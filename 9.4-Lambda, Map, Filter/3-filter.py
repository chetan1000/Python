nums = list(range(1, 11))
print("Numbers: ", nums)

even = lambda num: num % 2 == 0

print(even(5))
print(even(10000))

                                # applying filter on nums for even
result = filter(even, nums)     # it creates filter object at some address
print("Result using filter - even: ", result)         # printing filter object address
print(type(result))                                             # type 'filter'

print(list(result))                     # from 'nums' it can filters even numbers
print(tuple(result))
print(dict(result))
print(set(result))


# like map, 'filter'  is also Only ONCE time creates or it can be iterable once time.