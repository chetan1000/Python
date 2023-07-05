# Factorial of number
# n! = n!/(n-r)!

# 5! = 5*4*3*2*1
# 0! = 1
# 1! = 1

def iterFactorial(num):
    result = 1
    for item in range(1, num + 1):
        result = result * item

    return result

n=int(input("Enter any number: "))
out=iterFactorial(n)
print("Factorial of {} is {}".format(n,out))

# .format is a function on a String, we can pass the parameter (n, out), these parameter replaces {}=n and{}=out in
# print statement.

