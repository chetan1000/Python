runscored = 1

def localFunction():
    runscored = 2
    print("The value of runscored in localFunction(): ", runscored)


def globalFunction():
    global runscored
    runscored = 3
    print('The value of runscored in globalFunction()', runscored)


print('The value of runscored in main: ', runscored)                                    #runscored=1


localFunction()                                          # after executing localfunction, returned value runscored = 2 (the scope of value is valid within function only)
print("After calling localFunction, the value of runscored in main: ", runscored)           # runscored value in main = 1,


globalFunction()                                                                            #  after executing globalFunction, runscored = 3 , the scope is  valid throught whole program, runscored = 3
print("After calling globalVariable, the value of runscored in main: ", runscored)              # runscored in main becomes 1 to 3 due to Global


localFunction()                                                                                 # after executing, local function, runscored=2
print("After calling localFunction, the value of runscored in main: ", runscored)               # runscored = 3 in main, due to global


print('The value of runscored in main: ', runscored)                                            # runscored = 3, due to global



runscored = 7
print("the value of runscored:", runscored)


# Local variable scope present only within function
# Global variable scope is present throught the program
#
# In global variable,
#             ---> use them as CONSTANT, instead of variable
#             --->  Try to avoid use of global variable in python.

