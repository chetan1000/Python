# Function taking Function as a Parameter

def mySquare(num):
    return num * num

# mySquare(10)


# def myCube(n):
#     return n * n * n

def WrapperFunction(funcAsParm, num):                      #funcAsParm is not keyword we can give ny name.
    print("Type of funcAsParm: ", type(funcAsParm))
    return funcAsParm(num)                                  #calling mySquare() func


result = WrapperFunction(mySquare,5)    # Function call---> funcname(parameter)
                                        # it goes to WrapperFunction and takes mySquare as a parameter and num = 5 and
                                        # after that it will print the print statement in func definition and
                                        # then it went for mySquare function funcAsParm(num) mySquare(5) and returns 5*5 = 25 into result
print("Result: ",result)


# Functions are also first class objects in Python bcz takin function as parameter(object) then they are first class object.