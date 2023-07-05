def EmptyListAsParameter2(my_list=None):
    #if my_list is None:
    my_list=[]
    my_list.append('$')
    return my_list


r = EmptyListAsParameter2()
print("Returned output 1st iteration: ", r)
r1 = EmptyListAsParameter2()
print("Returned output 2nd iteration: ", r1)
r2 = EmptyListAsParameter2()
print("Returned output 3rd iteration: ", r2)
r3 = EmptyListAsParameter2([1,2,3])                # even we passed list but it will not take bcz in function definition "my_list=None"
print("Returned output 4th iteration: ", r3)
r4 = EmptyListAsParameter2([1,2,3])
print("Returned output 5th iteration: ", r4)

####################################################
# Returned output 1st iteration:  ['$']
# Returned output 2nd iteration:  ['$']
# Returned output 3rd iteration:  ['$']
# Returned output 4th iteration:  ['$']
# Returned output 5th iteration:  ['$']

# every time it set parameter my_list = None in function definition ,
# even we can pass anything into function call but if will not take