# packing example
def SumOfNumber(*args1):
    print("Args: ", args1)                      # args is not keyword, we can use any one.
    print("type(args): ", type(args1))


SumOfNumber(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


# Unpacking example
def printPlayerDetails(name, age, team):
    print("Player Details: ")
    print("Name: {}, Age: {}, Team: {}".format(name, age, team))      #whatever arguments are there in format(), they are replaced by {} curly base


printPlayerDetails("Virat", 33, "RCB")              # Function caller passing 3 arguments


msd = ("MS Dhoni", 37, "CSK")                  # tuple
printPlayerDetails(msd[0], msd[1], msd[2])          # func call   #indexing

printPlayerDetails(*msd)                      # Unpacking
                                                # printPlayerDetails(msd) ---> error, missing 2 reqd position arguments age & team



 # Unpacking:
    #  printPlayerDetails(*msd)---->when we used '*msd' @the Calling side, it break the Tuple into Individual Parameter

# Packing :
    #  def SumOfNumber(*args1):---->  when we used  or specify *  @the reciving side(func definition), it will collect them(parameter) all of them into Single "Tuple"


# there are NO POINTERS in Python

# breaking the Tuple is by .....> #Slicing-----------but it give tuples
                                 #spliting---------but it with dictionary
                                 #for loop-----we can't use this one
                                #Using Index------we can use

