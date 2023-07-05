def EmptyListAsParameter(my_list=None):
    if my_list is None:
        my_list=[]
    my_list.append('$')
    return my_list

r = EmptyListAsParameter()
print("Returned output 1st iteration: ", r)
r1 = EmptyListAsParameter()
print("Returned output 2nd iteration: ", r1)
r2 = EmptyListAsParameter()
print("Returned output 3rd iteration: ", r2)
r3 = EmptyListAsParameter([1,2,3])
print("Returned output 4th iteration: ", r3)
r4 = EmptyListAsParameter([1,2,3])
print("Returned output 5th iteration: ", r4)

##################################################
# Returned output 1st iteration:  ['$']
# Returned output 2nd iteration:  ['$']
# Returned output 3rd iteration:  ['$']
# every time when we called function with no argument passing, then if confition is True, then it will execute if condition and then function body and prints ['$']


# Returned output 4th iteration:  [1, 2, 3, '$']  # passing argument as list [1,2,3,$] in function call then the If condition becomes False then it not execute If condition and execute function body and appends '$' to our parameters in the list [1,2,3,'$']
# Returned output 5th iteration:  [1, 2, 3, '$']