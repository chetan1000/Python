# Dictionary Comprehension

# always returns result in Dictionary

# {1: 1, 2: 4, 3: 9, 4: 26, 5: 25, ...........}


    # normal method:
result = {}                                  # creating empty dict
for item in range(1, 11):
    result[item] = item * item              # result[item] : item * item ---> 1 : 1, 2: 4 so result[item] because of dictionary
print(result)


    # using Dictionary Comprehension:
result = {item: item * item for item in range(1, 11)}
print(result)

# another approch

print({item: item * item for item in range(1, 11)})



#####################################

s = "the quick brown box jumps over the lazy dog"

    # we want each letter or character as Key and Value as How much(count) of each character that appear in above string

# Using dict comprehension
result = {item: s.count(item) for item in s}
print(result)


#############################################
alphabets = ['a', 'b', 'c', 'd']
fruits = ['apple', 'banana', 'cherry', 'dates']

# using above two lists, create a dictionary using dictionary comprehension

result = {alphabets[item]: fruits[item] for item in range(0, 4)}
print(result)

# or
result = {alphabets[item]: fruits[item] for item in range(0,len(alphabets))}            #fruits[item]...error, list objects are not callable
print(result)

result = {alphabets[item]: fruits[item] for item in range(1,4)}
print(result)


####################################

alphabets = ['a', 'b', 'c', 'd']
fruits = ['apple', 'banana', 'cherry', 'dates']

# {'a': ('apple', 5), 'b': ('banana', 6), 'c': ('cherry', 6), 'd': ('dates', 5)}

result = {alphabets[item]: (fruits[item], len(fruits[item])) for item in range(0,4)}        #(fruits[item], len(fruits[item]))---> Tuple
print(result)