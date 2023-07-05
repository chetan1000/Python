def SumOfNumbers(a, b, c=0):
    print("Result: ", a + b)


SumOfNumbers(1, 2)


# Args
# *args makes tuple, if we use more arguments
# * is notation to tell that, receive them as tuple


def SumOfNumbers(*args):  # *args makes tuple, if we use more arguments
    print("Args: ", args)
    print("type(args): ", type(args))


SumOfNumbers(1, 2, 3)


# without * if we use args, it shows error, bcz there are two arguments, but we are considering only one by using args
#
# instead of receiving two arguments, they have created Tuple bcz we used *args in receiving argument
#

# why designer only choose "Tuple"? bcz Immutability

# there are NO POINTERS in Python

# Parameter
# A parameter is a variable that is declared in a function definition.
# It is used to receive the value that is passed to the function when it is called.
# Parameters are local to the function, which means that they can only be accessed within the function.
# Argument
# An argument is a value that is passed to a function when it is called.
# It is matched to the corresponding parameter in the function definition.
# Arguments can be of any type, including strings, numbers, lists, and dictionaries.
# The number of arguments that are passed to a function must match the number of parameters in the function's definition.
# Here is an example of a function definition with two parameters:
#
# Python
# def my_function(name, age):
#   print("Hello, {}. You are {} years old.".format(name, age))
