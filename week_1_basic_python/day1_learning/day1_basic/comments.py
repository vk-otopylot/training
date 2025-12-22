#This is single line comment - StandAlone

print('hello world')

print('hello world!!!') # This is single line Comment - InLine


#Multi-line Comment using Consecutive Single-Line Comments

# this
# is
# a
# multi-line comment

#Multi Line Comment Using Triple Quoted Strings

''' (you can use double quote as well)
this
is
a
multi-line comment
'''

#Docstrings

def hello(name):
    """

    name(str): person name to say hello

    return: None
    """
    print(f"hello {name}")


hello('vivek')

print(hello.__doc__)

help(hello)