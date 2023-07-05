def multipleUnpacking(*args):
    print("Args: ", args)
    print("Type of Args: ", type(args))


a = [1, 2, 3]                 #List
multipleUnpacking(*a)         #Unpacking


b = (4, 5, 6)                #Tuple
multipleUnpacking(*b)          # Unpacking


c = {4, 5, 6}             # Set
multipleUnpacking(*c)        #Unpack

r = range(100,105)          # Range
multipleUnpacking(*r)           # Unpack


print(*range(1, 6), sep=' ')
print(*range(1, 6), sep='\n')

# This feature is available on from Python 3.5