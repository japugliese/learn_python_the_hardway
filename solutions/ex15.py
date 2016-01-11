#ex15
#import from system argv
from sys import argv
#assgining script input file name to argv
script, filename = argv
#opens the file that is inputed to the command line
txt = open(filename)
#runs and prints file
print "Here's your file %r:" % filename
print txt.read()
#instead of using argv this uses raw iput to open the file
print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)
#without this next line it will not print
print txt_again.read()
