#ex15 more files
#importing argv and exist and file paths
from sys import argv
from os.path import exists
#creates script from_file and to_file to argv
script, from_file, to_file = argv
#displays that this will copy one file to another
print "Copying from %s to %s" % (from_file, to_file)
#Open from file and create in_file/ thn indata is read
#We could do these two lines on one, how?
indata=open(from_file).read()
#prints length of indata
print "the input file is %d bytes long" % len(indata)
#checks output file already exists then runs wiht input
print "does the output file exist? %r" % exists(to_file)
print "ready, hit RETURN to continue, CTRL-C to abort."
raw_input()
#then it outputs to_file with the write command
out_file=open(to_file,'w')
out_file.write(indata)

print "All right done."
#now lets close all the files
out_file.close()
