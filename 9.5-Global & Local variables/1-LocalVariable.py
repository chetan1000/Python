def myFunction():
    a = "LocalValue"
    print(a)
    print('Inside myFunction')


myFunction()         # Function call
print(a)             # name 'a' is not defined
                    # Error, the scope of 'a' is within myFunction(), we can't access outside the function
