def printStudentDetails1(**kwargs1):
    print("kwargs: ", kwargs1)
    print("type(kwargs): ", type(kwargs1))
    print("student details: Name: {}, Age: {}, Marks: {}, Stream: {}".format(kwargs1['name'], kwargs1['age'],
                                                                             kwargs1['marks'], kwargs1['stream']))


printStudentDetails1(name="Mary", age=15, marks=500, stream="CSE")
# name value type argument to convert dict
