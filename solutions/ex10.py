#lets play with quates and make sure that python understands
#creating a tabbed line
tabby_cat="\tI'm tabbed in."
#splitting a line right in the middle of a string
persian_cat="I'm split\non a line."
#
backslash_cat="I'm \\ a \\ cat."

fat_cat="""
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
#now lets print everything out to display it when we run
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

#lets try this; makes a spinning thing but I dont know how to stop it 
while True:
    for i in ["/","-","|","\\","|"]:
        print "%s\r" % i,
