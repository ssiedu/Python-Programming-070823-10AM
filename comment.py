#This is single line comment
print("Single line Comment")
"""This is
multiline
comment"""
print("Multiline comment")

def comment():
    """This is docstring Comment"""
    print("Docstring Comment")


comment()
print(comment.__doc__)
print(__doc__)
