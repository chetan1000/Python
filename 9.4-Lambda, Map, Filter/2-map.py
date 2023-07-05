nums = list(range(1, 11))
print("Numbers: ", nums)

Sq = lambda num: num * num

mobject = map(Sq, nums)             # it maps the Sq and nums, forms new object at some address
print(mobject)                      # it creats map object at some address
mobject = map(Sq, range(1, 11))     # it maps the Sq and range(1, 11), forms new object at some address
print(mobject)
print(type(mobject))                # <class 'map'> of type 'map'


print("List of Square of nums using Map: ", list(mobject))          # from 'map', we can only makes One time List or Tuple
# print(Sq)
# print(Sq(9))
print("Tuple of Square of nums using Map: ", tuple(mobject))        # output: () bcz from 'map' we can able to create only one time either list or tuple,
                                                                    # so we are already created list, so we not able to create Tuple
print("List of Square of nums using Map: ", list(mobject))       # output : []


                                        # it maps Sq and nums, and prints square of each number present in nums

# 'map' only creates an object at some address, we can only makes(creates) List or Tuple from that object , Only Once.



############################################################################################

nums = list(range(1, 11))
print("Numbers: ", nums)

even = lambda num: num % 2 == 0     # returns True or False

print(even(5))
print(even(8))

