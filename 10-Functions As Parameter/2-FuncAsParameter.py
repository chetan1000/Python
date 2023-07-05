def mySquare(num):
    return num * num


def myCube(n):
    return n * n * n


def iterFactorial(num):
    result = 1
    for item in range(1, num + 1):
        result = result * item

    return result


def WrapperFunction(funcAsParam, num):
    print("Type of funcAsParm: ", type(funcAsParam))
    return funcAsParam(num)


result = WrapperFunction(mySquare,5)
print("Result: ",result)


lstFunc = [mySquare, myCube, iterFactorial]     # Functions List  # func definition
for item in lstFunc:
    print("Result1: ",item(5))              # item(5) is Func call