# 5! = 5*4*3*2*1
# 1! = 1
# 0! = 1
# 5! = 5 * 4!
# 4! = 4 * 3!
# n! = n * (n-1)!

def recurFactorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * recurFactorial(num - 1)


n = int(input("Enter any Number: "))
out = recurFactorial(n)
print("Factorial of {} is {}".format(n, out))

# rf=recurFactorial
# 5! = 5 * rf(4)
# 4! = 4 * rf(3)
# 3! = 3 * rf(2)
# 2! = 2 * rf(1)
# 1! = 1

# ex: 5!      ---->  120
# 5! = 5 * 4!  ----> 5 * 24 = 120
# 4! = 4 * 3!   ---->4 * 6 = 24
# 3! = 3 * 2!   ----> 3 * 2 = 6
# 2! = 2 * 1!   ----> 2 * 1 = 2
# 1! = 1      ---->  1

# A function calling is limit, like how many times a function can be call itself, we can define in setting.
#
# By default, recursion function call to define 1000 times if we written function, which is going behind 1000 times,
# it shows, Recursion error that Maximum recursion depth exceed in comparision.
