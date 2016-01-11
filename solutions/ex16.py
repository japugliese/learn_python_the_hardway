#Exercise16: Reading and Writing Files
#import from system argv
from sys import argv
#create file name in command line script
script, filename = argv
#lists the file name using %r 
print "We're going to erase %r." % filename
print "If you dont waant that hit CTRL-C (^C)."
print "If you do want that hit RETURN."
#okay so now by hitting enter 
raw_input("?")
#we are going to open the filename under the 'w' writable
print "opening the file..."
target=open(filename,'w')
#truncating is going to empty the entire file
print "Truncating the file. Goodbye!"
target.truncate()
print "Now I'm going to ask you for three lines"
#using raw input we can create three new lines
line1=raw_input("line 1: ")
line2=raw_input("line 2: ")
line3=raw_input("line 3: ")
#
print "I'm going to write these to the file."
#now we are going to write this into the new file
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close
