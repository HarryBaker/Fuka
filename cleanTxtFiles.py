__author__ = 'loaner'
from sys import argv
#import nltk

print("Hello World")

raw_file_name = raw_input("Enter the name of your file: ");
file_name = raw_file_name + ".txt";
f = open(file_name, "r")
f2 = open((raw_file_name + "2.txt"), "w")

while 1:
    char = f.read(1)
    if not char: break
    if char.isalpha() or char.isspace() or char == '.' : f2.write(char.lower());
    
f2 = open((raw_file_name + "2.txt"), "r")
f3 = open((raw_file_name + "3.txt"), "w")

wrote_word = False

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