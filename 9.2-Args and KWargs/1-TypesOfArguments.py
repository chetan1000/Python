def namedArgumentFunction(a,b,c):
    print("The values are a: {},b: {},c: {}".format(a, b, c))


namedArgumentFunction(100, 200, 300)
                # Positional Arguments
                # a->100,b->200,c->300


namedArgumentFunction(c=3,a=1,b=2)
                # Named Arguments
                # ->1,b->2,c->3


namedArgumentFunction(100, b=102, c=103)
                # mix of positional + Named
                # a->100,b->102,c->103

# Positional Arguments define first, then only Named Arguments
# This is Order in Python

#namedArgumentFunction(201, a=202, c=203)
        # Mix of Position + Mixed
        # a = 201  and 202, c=203
       # TypeError: namedArgumentFunction() got multiple values for argument 'a'


#namedArgumentFunction(b=600, 500, c=103)
            # Mix of position + Name
            # Error : positional argument is not first
            # positional argument follows keyword argument


# python does not allow to pass Positional Argument after the keyword arguments
