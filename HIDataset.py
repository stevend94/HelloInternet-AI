import os
import glob
import io

from torchtext import data


class HelloInternetDataset(data.Dataset):

    @staticmethod
    def sort_key(ex):
        return len(ex.text)

    def __init__(self, path, text_field, label_field, **kwargs):
        """Create an HI dataset instance given a path and fields for classifying whether it's grey or brady speaking.
        Args:
            path: Path to the dataset's highest level directory
            text_field: The field that will be used for text data.
            label_field: The field that will be used for label data.
            Remaining keyword arguments: Passed to the constructor of
                data.Dataset.
        """
        fields = [('text', text_field), ('label', label_field)]
        examples = []

        for label in ['grey', 'Brady']:
            for fname in glob.iglob(os.path.join(path, label, '*.txt')):
                with io.open(fname, 'r', encoding="utf-8") as f:
                    text = f.readline()
                    
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                if len(line) > 0:
                    if line.split()[0] == '[Grey]':
                        text = " ".join(line.split()[1:])
                        label = "Grey"
                        examples.append(data.Example.fromlist([text, label], fields))
                        
                    elif line.split()[0] == '[Brady]':  
                        text = " ".join(line.split()[1:])
                        label = "Brady"
                        examples.append(data.Example.fromlist([text, label], fields))
                    

        super(HelloInternetDataset, self).__init__(examples, fields, **kwargs)

    @classmethod
    def splits(cls, text_field, label_field, root='data',
               train='train', test='test', **kwargs):
        """Create dataset objects for splits of the HI dataset.
        Args:
            text_field: The field that will be used for the sentence.
            label_field: The field that will be used for label data.
            root: Root dataset storage directory. Default is '.data'.
            train: The directory that contains the training examples
            test: The directory that contains the test examples
            Remaining keyword arguments: Passed to the splits method of
                Dataset.
        """
        return super(HelloInternetDataset, cls).splits(
            root=root, text_field=text_field, label_field=label_field,
            train=train, validation=None, test=test, **kwargs)

    @classmethod
    def iters(cls, batch_size=32, device=0, root='.data', vectors=None, **kwargs):
        """Create iterator objects for splits of the HIdataset.
        Args:
            batch_size: Batch_size
            device: Device to create batches on. Use - 1 for CPU and None for
                the currently active GPU device.
            root: The root directory that contains the imdb dataset subdirectory
            vectors: one of the available pretrained vectors or a list with each
                element one of the available pretrained vectors (see Vocab.load_vectors)
            Remaining keyword arguments: Passed to the splits method.
        """
        TEXT = data.Field()
        LABEL = data.Field(sequential=False)

        train, test = cls.splits(TEXT, LABEL, root=root, **kwargs)

        TEXT.build_vocab(train, vectors=vectors)
        LABEL.build_vocab(train)

        return data.BucketIterator.splits(
            (train, test), batch_size=batch_size, device=device)