import os 
import time 

path = "data/raw_transcripts"
files = os.listdir(path)

def isTimeFormat(input):
    """
        Check if the input is a time format
    """
    try:
        if len(input.split(':')) == 2:
            time.strptime(input, '%M:%S')
        else:
            time.strptime(input, '%H:%M:%S')
        return True
    except ValueError:
        return False
    
    
def process_text(text):
    """
        Process the HI transcripts by removing time stamps and adding label for each speaker.
    """
    
    processed_text = []

    for i, line in enumerate(text):
        if len(line.split()) > 1:
            name = line.split()[0]
            timestamp = line.split()[1]

            if name == 'Brady' and isTimeFormat(timestamp):
                processed_text.append('[Brady] ' + text[i+1])

            if name == 'Grey' and isTimeFormat(timestamp):
                    processed_text.append('[Grey] ' + text[i+1])   
                    
    return processed_text


def get_text(path):
    """
        Get text from transcript and process
    """
    text = []

    with open(path, "r") as f:
        for line in f:
            if len(line.strip()) > 0:
                text.append(line.strip())
                
    processed_text = process_text(text)
    
    return processed_text


if __name__ == "__main__":
    
    data_dict = {}
    for file in os.listdir(path):
        name = file.split('_otter')[0]
        text = get_text(path + '/' + file)
        data_dict[name] = text
        
    for key in data_dict:
        with open("hi_all_text.txt", "a") as f:
            f.write("<|startoftext|> \n")
            f.write("Title - " + str(key) + '\n')
            for line in data_dict[key]:
                f.write(line + '\n')
            f.write("<|endoftext|> \n")

