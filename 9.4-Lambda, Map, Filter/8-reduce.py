from functools import reduce        # functools is file, reduce is function written in functools file

nums = list(range(1, 11))
print("Numbers: ", nums)


addNo = lambda x,y: x + y
# print(addNo(100, 200))


result = reduce(addNo, nums)          # reduce(Function, sequence)
print("Result: ", result)              # reduce function will work on 2 inputs only
                                        # addNo is function applying on numbs by the reduce

multiply = lambda x, y: x * y

result = reduce(multiply, nums)
print("Result: ", result)



# lambda for 3 inputs only.

f = lambda x, y, z: x + y + z
print(f(100, 200, 300))
print(f)