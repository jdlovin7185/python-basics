lunch_menu = (
    "Sup", "hello", "Bonjour", "bro-beans", "suuuhh dude"
)

print(lunch_menu[2])

# you can't write to a tuple since it is immutable
# lunch_menu[1] = "Hey Jack"

# unpacking the tuple and assigning it to different variables
# in order to unpack all the elements, you have to have the
# same amount of variables as the tuple has
a, b, c, d, e = lunch_menu

# now you can change the value of the variable
b = "HELLO"

print(b)
