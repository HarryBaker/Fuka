# A program that cleans text files when given raw input in the following manner:
# Remove all characters except letters, spaces, and periods
# Convert all letters to lowercase

__author__ = 'loaner'
from sys import argv

class Cleaner:
    def __init__(self, input):
        raw_file_name = raw_input(input);
        file_name = raw_file_name + ".txt";
        # Access the raw file
        f = open(file_name, "r")
        f2 = open((raw_file_name + "_intermediary.txt"), "w")
        
        
        
    # First cleanup (by character):     

    # Cleaning every character that is not a letter, space, or period
    # Converting all letters to lowercase
        while 1:
            char = f.read(1)
            if not char: break
            if char.isalpha() or char.isspace() or char == '.' : f2.write(char.lower());
    
        f2 = open((raw_file_name + "_intermediary.txt"), "r")
        f3 = open((raw_file_name + "_clean.txt"), "w")

        wrote_word = False
        
        
    # Second cleanup:         

    # Remove unneccessary spaces and newlines longer than one character that was not possible in the previous clean up step
    # Remove words that are shorter than 2 characters
        for line in f2:
            line = line.rstrip()
            words = line.split()
            for word in words:
                wrote_word = False
                if len(word)>2:
                    f3.write(word + " ")
                    wrote_word = True
            if(wrote_word):
                f3.write("\n")

        f.close()
        f2.close()
        f3.close()

# Works Cited:
# http://www.tutorialspoint.com/python/python_files_io.htm
# http://learnpythonthehardway.org/book/ex15.html
# http://www.java2s.com/Code/Python/File/Openafileandreadcharbychar.htm
# http://pymbook.readthedocs.org/en/latest/file.html
# http://stackoverflow.com/questions/29359401/open-a-file-split-each-line-into-a-list-then-for-each-word-on-each-line-check
