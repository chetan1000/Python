# Lambda Function
# is a simple function
# used for simple operations
# Anonymous Functions
# Function which have got NO Names
# They are used to write ONE-LINE Functions.
# for lambda function, we don't have to define def, function name and not have any return keyword.
# lambda is an another function, without writing Function definition, we can write in single line.


# creating function using normal method
def mySquare(num):
    return num * num


print(mySquare(9))

# square of number using Lambda Function
# for lambda function, we don't have to define def, function name and not have any return keyword.

f = lambda num: num * num    # takes input as num and returns num * num
print(f)                       # gives there is lambda function in this address
print(type(f))                # lambda is function type of 'class Function'
result = f(10)                       # to call function
print("Square of number: ", result)


print("Square of number: ", (lambda num: num * num)(5))         # function and input in print statement

print("Square of number: ", (lambda num: num * num)(int(input("Enter any number: "))))         # function and user entered input in print statement


# finding max of two number using lambda

z = lambda x, y: x if x > y else y              # if else condition in lambda function
print("Max of 3, 5: ", z(3, 5))
