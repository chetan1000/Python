def printStudentDetails(**d):                 # packing
    print("kwargs: ", d)
    print("type(kwargs): ", type(d))
    print("id(kwargs: ", id(d))


d = {'name': 'john', 'Stream': 'ECE', 'age': 18, 'marks': 625}       # dict as variable
printStudentDetails(**d)                                  # Unpacking
                                # it is already dictionary, they why ** is required?
                                #  printStudentDetails(**d) , in function call, **d breaks dict into 4 keyword(named) arguments separately, (UNPACK)
                                #  then these arguments passed to the function defintion def printStudentDetails(**d):
                                #  there it will convert them(argument) into Dict.(PACK)



# printStudentDetails(d)                 #error, bcz d is already dictionary, from this dict can't create again dict
# printStudentDetails(d.items())         # TypeError: printStudentDetails() takes 0 positional arguments but 1 was given
id(d)