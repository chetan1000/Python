nums = list(range(1, 11))
print("Numbers: ", nums)

even = lambda num: num % 2 == 0

print(even(5))
print(even(10000))

                                # applying filter on nums for even
result = filter(even, nums)
print("Result using filter - even: ", result)
print(type(result))

print(set(result))
print(tuple(result))