# Positional + Keyword - Only Arguments

# Before '/' ---> Positional
# After '*' ---> Keyword(Named)

            # Available only on python 3.8


def PositionalKeywordArguments(a, b, /, z, w, *, x, y):
    print("a: {},b: {},z: {},w: {}, x: {},y: {}".format(a, b, z, w, x, y))


PositionalKeywordArguments(1, 2, 3, 4, x=5, y=6)
                                                    # before '/' are positional, i.e 1, 2
                                                    # after '*' are Keyword(named), i.e, x=5, y=6
                                                    # z & w may be anything
                                                    # between '/' and '*' may be anything

PositionalKeywordArguments(1, 2, z=3, w=4, x=5, y=6)
                                                        # 1, 2 positional
                                                        # x=5, y=6 keyword(named)
                                                        # after * are keyword


PositionalKeywordArguments(1, 2, 3, 4, 5, 6)
                                                        # Error, x, y needs to pass the named(keyword) arguments.
                                                        # TypeError: PositionalKeywordArguments() takes 4 positional arguments but 6 were given



# Python is PASS BY OBJECT not a VALUE or NAME