#
def myFunction():
    global temp                            # we declared it as Global Inside the Function, so update it as Global we need to execute Function first
    temp = 'Global Variable'                            # created temp & defined it as 'Global'
    print('value of temp INSIDE myFunctions: ', temp)


# print('value of temp OUTSIDE myFunction: ', temp)    # program starts running from here, it doesn't know what is 'temp'
                                            # even though we declared 'temp' as Global, but we are not call the function and inside function we assigned temp as Global
                                                # when function get called & executed then only temp becomes global , having assigned value

myFunction()
print('value of temp OUTSIDE myFunction: ', temp)

