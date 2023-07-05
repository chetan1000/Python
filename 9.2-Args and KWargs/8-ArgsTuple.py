def printStudentDetails(*d):
    print("args: ", d)
    print("type(args): ", type(d))
    print("id(args: ", id(d))


d = {'name': 'john', 'Stream': 'ECE', 'age': 18, 'marks': 625}      #dict
print(d.keys())
printStudentDetails(d.keys())
printStudentDetails(d.values())
printStudentDetails(d.items())
printStudentDetails(d)
printStudentDetails(*d)
print("id(d): ", id(d))


# printStudentDetails("name"= 'john', "Stream"= 'ECE', "age"= 18, "marks" = 625)   #Error, expression cannot contain assignment

