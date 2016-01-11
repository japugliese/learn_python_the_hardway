#Ex19: Functions and Variables
#creating a function
#start by defining the function
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    #now print the first line of the function value
    print "you have %d chesses!" % cheese_count
    #now print the second line of the function value
    print "you have %d boxes of crackers!" % boxes_of_crackers
    print "man that's enough for a party!"
    print "get a blanket.\n"
#one way to call the function
print "we can just give the function numbers directly:"
cheese_and_crackers(20,30)
#another way to call the function
print "OR we can use variables from our script"
amount_of_cheese = 10
amount_of_crackers=50
#this is actually calling the function
cheese_and_crackers(amount_of_cheese,amount_of_crackers)
#now do it all at once
print "We can even do math inside too:"
cheese_and_crackers(10+20,5+6)
#now do it all together
print "and we can combine the two, math and variables"
cheese_and_crackers(amount_of_cheese+100,amount_of_crackers+1000)

