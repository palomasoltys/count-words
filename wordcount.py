"""Count words in file."""
import sys
def word_count(file):
    the_file_test = open(file)
    word_count = {}
    for line in the_file_test:
        line = line.rstrip()
        words = line.split() 
        for word in words:
            word = word.lower()
            word = word.strip(",.!?;':_\"")
            word_count[word] = word_count.get(word, 0) + 1
    return word_count
try:
    file = sys.argv[1] 
    print(word_count(file))
except:
    print('Invalid file name') 

def tokenize(file):
    the_file = open(file)
    for line in the_file:
        line = line.rstrip()
        words = line.split()
    return words    

def count_words(words):
    word_count = {}
    for word in words:
        word = word.lower().strip(",.!?;':_\"")
        word_count[word] = word_count.get(word, 0) + 1
    return word_count 

my_words = tokenize('test.txt') 
print(count_words(my_words))      

    

