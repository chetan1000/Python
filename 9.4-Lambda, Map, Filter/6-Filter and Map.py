nums = list(range(1, 11))
print("Numbers: ", nums)

even = lambda num: num % 2 == 0

print(even(5))
print(even(10000))

                        # applying filter
result = filter(even, nums)
print("Result using filter-even: ", result)
print(type(result))
print(list(result))
print(tuple(result))


                        # applying map
result = map(even, nums)
print("Result using map-even: ", result)
print(type(result))
print(list(result))                 # it returns, [False, True, False, True, False, True, False, True, False, True]
                                    # for even numbers-True, odd numbers- False
print(tuple(result))