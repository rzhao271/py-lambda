d = lambda f: f(f)

fact = lambda f: lambda x: 1 if x == 0 else x * d(f)(x - 1)
assert d(fact)(5) == 120
assert (lambda f: lambda x: 1 if x == 0 else x * f(f)(x - 1))(lambda f: lambda x: 1 if x == 0 else x * f(f)(x - 1))(5) == 120

Z = lambda f: (lambda x: f(lambda v: x(x)(v)))(lambda x: f(lambda v: x(x)(v)))

fact1 = lambda f: lambda x: 1 if x == 0 else x * f(x - 1)
assert Z(fact1)(5) == 120
assert ((lambda f: (lambda x: f(lambda v: x(x)(v)))(lambda x: f(lambda v: x(x)(v))))(lambda f: lambda x: 1 if x == 0 else x * f(x - 1)))(5) == 120