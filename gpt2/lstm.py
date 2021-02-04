import torchtext
from torchtext import data
from torchtext.data.dataset import check_split_ratio
import io

import torch

class HILanguageModelDataset(data.Dataset):
    """Defines a dataset for language modeling."""

    def __init__(self, path, text_field, newline_eos=True,
                 encoding='utf-8', **kwargs):
        """Create a LanguageModelingDataset given a path and a field.
        Args:
            path: Path to the data file.
            text_field: The field that will be used for text data.
            newline_eos: Whether to add an <eos> token for every newline in the
                data file. Default: True.
            Remaining keyword arguments: Passed to the constructor of
                data.Dataset.
        """
        fields = [('text', text_field)]
        text = []
        with io.open(path, encoding=encoding) as f:
            for line in f:
                text += text_field.preprocess(line)
                if newline_eos:
                    text.append(u'<eos>')

        examples = [data.Example.fromlist([text], fields)]
        super(HILanguageModelDataset, self).__init__(
            examples, fields, **kwargs)
        
        
    def split(self, split_ratio=0.7, text_field=None):
        """Create train-test(-valid?) splits from the instance's examples.
        Args:
            split_ratio (float or List of floats): a number [0, 1] denoting the amount
                of data to be used for the training split (rest is used for test),
                or a list of numbers denoting the relative sizes of train, test and valid
                splits respectively. If the relative size for valid is missing, only the
                train-test split is returned. Default is 0.7 (for the train set).
            stratified (bool): whether the sampling should be stratified.
                Default is False.
            strata_field (str): name of the examples Field stratified over.
                Default is 'label' for the conventional label field.
            random_state (tuple): the random seed used for shuffling.
                A return value of `random.getstate()`.
        Returns:
            Tuple[Dataset]: Datasets for train, validation, and
            test splits in that order, if the splits are provided.
        """
        train_ratio, test_ratio, val_ratio = check_split_ratio(split_ratio)
        
        fields = [('text', text_field)]
        
        size = len(self.examples[0].text)
        
        index = int(size *train_ratio)
        train_text = self.examples[0].text[:index]
        train_data = [data.Example.fromlist([train_text], fields)]
        
        val_text = self.examples[0].text[index:index + int(size *val_ratio)]
        val_data = [data.Example.fromlist([val_text], fields)]
        
        index = index + int(size *val_ratio)
        test_text = self.examples[0].text[index:index + int(size *test_ratio)]
        test_data = [data.Example.fromlist([test_text], fields)]

        splits = tuple(torchtext.data.Dataset(d, self.fields)
                       for d in (train_data, val_data, test_data) if d)

        # In case the parent sort key isn't none
        if self.sort_key:
            for subset in splits:
                subset.sort_key = self.sort_key
        return splits
    
    
class LanguageModel(torch.nn.Module):
    def __init__(self, dims, vocabulary, num_layers, init_val, dropout):
        super(LanguageModel, self).__init__()
        
        self.embeddings = torch.nn.Embedding(vocabulary, dims)
        self.dropout = torch.nn.Dropout(dropout)
        self.lstm = torch.nn.LSTM(dims, dims, num_layers = num_layers, dropout=dropout)
        self.linear = torch.nn.Linear(dims, vocabulary)
        self.init_weights(init_val)
        
    def detach_states(self, states):
        return tuple([h.detach() for h in states])
    
    def init_weights(self, init_val = 0.05):
        self.embeddings.weight.data.uniform_(-init_val, init_val)
        for w in self.lstm.all_weights:
            for a in w:
                a.data.uniform_(-init_val, init_val)
                
        # set lstm forget gate to zeros 
        for l in self.lstm.all_weights:
            l[2].data[self.lstm.hidden_size:int(self.lstm.hidden_size*2)].fill_(0)
            l[3].data[self.lstm.hidden_size:int(self.lstm.hidden_size*2)].fill_(0)
        
        self.linear.weight.data.uniform_(-init_val, init_val)
        
    def forward(self, x, states, train=False):
        self.training = train
        tensor = self.embeddings(x)
        
        if train:
            tensor = self.dropout(tensor)
            
        tensor, state = self.lstm(tensor, states)
        if train:
            tensor = self.dropout(tensor)
            
        tensor = tensor.view(-1, tensor.size(2))
            
        # tensor = torch.nn.functional.log_softmax(self.linear(tensor), dim=1)
        tensor = self.linear(tensor)
        
        return tensor, self.detach_states(states)