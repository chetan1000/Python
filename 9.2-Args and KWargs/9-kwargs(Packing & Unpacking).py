def printStudentDetails(name, age, marks, stream):  # Function taking 4 arguments(parameter)   #PACKING
    print("Student details:")
    print("Name: {}, Age: {}, Marks: {}, Stream: {}".format(name, age, marks, stream))


printStudentDetails("Chetan", 26, 625, "Data Science")  # passing 4 arguments

d = {'name': 'Pragati', 'stream': 'IAS', 'age': 26, 'marks': 1000}  # dict
printStudentDetails(**d)  # UNPACKING(**d breaks dict into 4 arguments and then passing into function definition)


####################################################################################################

def printStudentDetails2(name, age, marks, stream):  # Function taking 4 arguments(parameter)
    print("Student details:")
    print("Name: {}, Age: {}, Marks: {}, Stream: {}".format(name, age, marks, stream))


a = {'name': 'chetan', 'stream': 'IAS', 'age': 26, 'marks': 1000}
printStudentDetails2(*a)                   # NOT CORRECT WAY

# it breaks Dict but taking only Keys
# output---> Name: name, Age: stream, Marks: age, Stream: marks