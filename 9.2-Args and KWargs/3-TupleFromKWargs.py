def printStudentDetails(*chetan):             # for tuple creation
    print("kwargs: ",chetan)
    print("type(kwargs): ", type(chetan))


# printStudentDetails(name='mary', age=25, marks=500, stream='CSE')
                                                                    # if we use this , it shows error
                                                                    # TypeError: printStudentDetails() got an unexpected keyword argument 'name'


printStudentDetails('mary',15,500,'CSE')




# for Dictionary creation, we must pass named argument in the function

# can we store dict into variable?----> kwargs becomes variable.

# From key can we access dict ?




