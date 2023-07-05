
def PositionalArguments(a, b, /, z, x, y):
    print("a: {},b: {},z: {},x: {},y: {}".format(a, b, z, x, y))

PositionalArguments(1, 2, 3, 4, 5)
PositionalArguments(1, 2, z=3, y=5, x=4)
PositionalArguments(a=1, b=2, z=3)            # 1, 2 must be positional