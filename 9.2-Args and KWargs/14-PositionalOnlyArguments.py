#Positional-Only Arguments
            # available ONLY from python 3.8


# Rule : before '/'all should be positional arguments, after '/' we can specify named or positional arguments


def positionalArguments(a, b, /, z):
    print("a: {},b: {},z: {}".format(a, b, z))

                                        # before '/' we can pass via Positional Arguments only


positionalArguments(1, 2, 3)        # 1, 2 are positional,

positionalArguments(1, 2, z=3)      # 1, 2 are positional, z=named

positionalArguments(a=1, b=2,z=3)    # here 1, 2 are named
                                    # Error, positionalArguments() got some positional-only arguments passed as keyword arguments: 'a, b'



# Use: if we have more arguments, in that we can make Mandatory arguments and some of them make Not-Mandatory arguments




