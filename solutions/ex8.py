#creating a fromatted string
formatter="%r %r %r %r"
#ok now we are using formatter as a variable to create strings within strin
#so we put 1-4 into the string
print formatter %(1,2,3,4)
#again putting 1-4 into the string
print formatter %("one","two","three","four")
#putting in true or false into the string
print formatter %(True, False, False, True)
#putting a string within a string within strings
print formatter %(formatter, formatter, formatter, formatter)
#With this line gets broken apart because of the commas
print formatter %(
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said good night",
    )
