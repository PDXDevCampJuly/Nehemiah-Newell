# This is just a quick program to take inputs and plug it into a 'story'
# and then print it out.

# We start the story
article = "The "

# start asking for information from the user
theInput = input("Please enter a dark wizard: ")
# and concantitate it.
article += theInput + " unleashed a awful "

# start asking for information from the user
theInput = input("Please enter a monster: ")
# and concantitate it.
article += theInput + " who ate all the  "

# start asking for information from the user
theInput = input("Please enter the victims ")
# and concantitate it.
article += theInput + " and "

# start asking for information from the user
theInput = input("Please enter a action ")
# and concantitate it.
article += theInput + "."

# and output
print("\n\n")
print(article)
print("\n\n")