#creating different variables and strings
my_name='Jesse Pugliese'
my_age=27 #no lie
my_height=73 #in inches
my_weight=180 #in lbs.
my_eyes='blue'
my_teeth='white'
my_hair='brown'
#okay now lets print these out by using the strings we just made
#use %s to print a string be sure to identify the string at the end of line
print "lets talk about %s." %my_name
#%d will print a number string
print "he's %d inches tall." %my_height
print "he's %d pounds." %my_weight
print "actually not that heaavy."
print "he's got %s eyes and %s hair." %(my_eyes,my_hair)
print "his teeth are usually %s depending on his coffee." %my_teeth

#this line is kind of tricky
print "if I add %d, %d, and %d i get %d." % (
        my_age, my_height, my_weight, my_age+my_height+my_weight)
