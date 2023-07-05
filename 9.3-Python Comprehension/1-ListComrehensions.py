# Approch 1

result = []
for item in range(1, 11):
    result.append(item * item)

print(result)

# Approch 2 (using list comprehension)

result = [item * item for item in range(1, 11)]
print(result)
# for loop inside the list
# the item * item before the for loop becomes elements of the list.


# Approch 3

print([item * item for item in range(1, 11)])

# "Every List Comprehension code can be written back to a normal code.",
#  but not every normal code can written in List Comprehension code.

# List comprehension works faster than normal code.

# Every result is returning in List.


# Generate a list of numbers between 1 and 20, which are divisible by 3, use list comprehension method

result = [item for item in range(1, 21) if item%3 == 0]
print(result)
                                                            # if item%3 == 0 --->condition
                                                            # for item in range(1, 21)---> iteration
                                                            # item ---> expression


# Given the Subject = "MATHEMATICS", print all the Consonants in a list.
# ['M', 'T', 'H', 'M', 'T', 'C', 'S']

    # using normal method:
result = []
for conso in "MATHEMATICS":
    if conso not in "AEIOU":
        result.append(conso)

print(result)


    # using List Comprehension
print([item for item in "MATHEMATICS" if item not in "AEIOU"])



########################################

websites = ["Amazon", "Flipkart", "Paytm"]

# using List Comprehension generate below list
# ['www.Amazon.com', 'www.Flipkart.com', 'www.Paytm.com']

result = ['www.'+item+'.com' for item in websites]
print(result)

##########################

websites = ["Amazon", "Flipkart", "Paytm", 'Snapdeal']
extensions = ['com', 'org', 'in']

result = ['www.'+web+'.'+ext for web in websites for ext in extensions]
print(result)


###########################

s = "Welcome to the world of Python programming"

# split
lstWords = s.split(" ")                   # split s with space
print(lstWords)


##################################
# Write a program to generate like below output
lstWords = ['Welcome', 'to', 'the', 'world', 'of', 'Python', 'programming']
# [('welcome', 7), ('to', 2), ('the', 3), ..........]     we need to have result in list and
# that list contains element and each element as tuple consists of (word, lengthOfWord)
# List of Tuples along with length

    # using normal method:
result = []                        #  empty list creating
for item in lstWords:
    result.append((item, len(item)))    # appending empty list with Tuple  .append((item, len(item))) thats why we used ()
   # result.append([item, len(item)])  # appending list
   # result.append({item, len(item)})  # appending set
print(result)


    # using List Comprehension
result = [(item, len(item)) for item in lstWords]
print(result)


##########################
s = "Welcome to the world of Python programming"
lstWords = ['Welcome', 'to', 'the', 'world', 'of', 'Python', 'programming']
# [(0, 'Welcome', 7), (1, 'to', 2), (2, 'the', 3), (3, 'world', 5), (4, 'of', 2), (5, 'Python', 6), (6,'programming', 11)]
# list consists of elements where each element as tuple (index, word, lenOfWorf)


    # using normal method
result = []
for (index, item) in enumerate(lstWords):
    result.append((index, item, len(item)))
print(result)


# using List comprehension
result = [(index, item, len(item)) for index, item in enumerate(lstWords)]      # using enumerate() we can get (index, item)
print(result)
