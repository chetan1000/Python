# kwargs --> Dictionary

def printStudentDetails(**kwargs):
    print("kwargs: ", kwargs)
    print("type(kwargs): ", type(kwargs))


# printStudentDetails("Mary", 15, 500, "CSE")
# TypeError: printStudentDetails() takes 0 positional arguments but 4 were given


printStudentDetails(name='Mary', age=25, marks=500, stream='CSE')
                                            # named arguments
                                            # **kwargs creates Dict and it is only possible if Named Arguments pass
                                            # printStudentDetails('name'='Mary', 'age'=25, 'marks'=500, 'stream'='CSE')
                                                    # error, expression cannot contain assignment

                        # printStudentDetails() function call having named arguments, then the cursor will go to Function definition and
                        # there **kwargs creates Dictionary using these arguments.


# kwargs --> Not Pointer
# kwargs --> notation to tell that we are receiving all arguments as Dictionary or as collection of Key:Value pair



