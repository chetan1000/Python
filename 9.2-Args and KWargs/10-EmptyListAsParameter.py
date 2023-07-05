def EmptyListAsParameter(my_list=[]):      # Don't use Empty List [] as parameter in function definition
    my_list.append("$")
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



###############################################################
# Returned output 1st iteration:  ['$']    firstly the function has [] as parameter, we called function with no argument passing, it simply execute funtion body with list containing '$'
# Returned output 2nd iteration:  ['$', '$']     alredy list consists ['$'] then we called function with no argument passing, so it appended '$'
# Returned output 3rd iteration:  ['$', '$', '$'] alredy list consists ['$','$'] then we called function with no argument passing, so it appended '$'
# Returned output 4th iteration:  [1, 2, 3, '$']     we passed argument as list [1,2,3] and then it execute function body and appends '$' intothe list
# Returned output 5th iteration:  [1, 2, 3, '$']