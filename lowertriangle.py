Z = lambda f: (lambda x: f(lambda v: x(x)(v)))(lambda x: f(lambda v: x(x)(v)))

line = lambda f: lambda x: '' if x == 0 else '*' + f(x - 1)
assert Z(line)(1) == '*'
assert Z(line)(5) == '*****'

multiline = lambda f: lambda x: '' if x == 0 else Z(line)(x) + '\n' + f(x - 1)
assert Z(multiline)(1) == '*\n'
assert Z(multiline)(5) == '*****\n****\n***\n**\n*\n'

# Comment out if you only want to run asserts
# This is just the previous functions combined with a bit of interactivity
# print((lambda f: lambda x: '' if x == 0 else (lambda f: lambda x: '' if x == 0 else '*' + f(f)(x - 1))(lambda f: lambda x: '' if x == 0 else '*' + f(f)(x - 1))(x) + '\n' + f(f)(x - 1))(lambda f: lambda x: '' if x == 0 else (lambda f: lambda x: '' if x == 0 else '*' + f(f)(x - 1))(lambda f: lambda x: '' if x == 0 else '*' + f(f)(x - 1))(x) + '\n' + f(f)(x - 1))(int(input("Enter a number n >= 0: "))), end="")
