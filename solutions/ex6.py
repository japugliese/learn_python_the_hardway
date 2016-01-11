#using short names for variables and strings.
x="There are %d types of people." %10
binary="binary"
do_not="don't"
y="Those who know %s and those who %s." %(binary,do_not)
#now lets print out the joke
print x
print y

#now print the joke with some extras
print "I said: %r." %x
print "I alos said: '%s'." %y
#this is where we put a string within a string
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
#see we put the string inside the string
print joke_evaluation %hilarious

w="this is the left side of..."
e="a string with a right side."

print w+e

