# import sys
# sys.setrecursionlimit(10000)
# get_lambs = lambda g: lambda f: [1 + g(f()), 0][callable(f)]
# gen_nums = lambda g: lambda h: [g(h - 1) + [h], []][h > 0]
# Z = lambda f: (lambda x: f(lambda v: x(x)(v)))(lambda x: f(lambda v: x(x)(v)))
# m = lambda g: lambda n: lambda r: [lambda: not (n - r), lambda: g(n - r)(r)][n - r > 0]()
# u = lambda g: lambda a: lambda b: lambda c: [lambda: c, lambda: g(a - 1)(b)(c + b)][a > 0]()
# f = lambda g: lambda n: lambda s: lambda a: lambda b: [[[str(n), s[:4]][(Z)(m)(n)(a)], s[4:]][(Z)(m)(n)(b)], s[:]][(Z)(m)(n)((Z)(u)(a)(b)(0))]
# d = lambda g: lambda n: lambda h: [lambda: None, lambda: print((Z)(f)(h + 1)("fizzbuzz")(3)(5)) or g(n)(h + 1)][n - h > 0]()
# (Z)(d)(100)(0)

# Z = lambda f: (lambda x: f(lambda v: x(x)(v)))(lambda x: f(lambda v: x(x)(v)))
# m = lambda g: lambda n: lambda r: [lambda: not (n - r), lambda: g(n - r)(r)][n - r > 0]()
# u = lambda g: lambda a: lambda b: lambda c: [lambda: c, lambda: g(a - 1)(b)(c + b)][a > 0]()
# f = lambda g: lambda n: lambda s: lambda a: lambda b: [[[str(n), s[:4]][(lambda f: (lambda x: f(lambda v: x(x)(v)))(lambda x: f(lambda v: x(x)(v))))(lambda g: lambda n: lambda r: [lambda: not (n - r), lambda: g(n - r)(r)][n - r > 0]())(n)(a)], s[4:]][(lambda f: (lambda x: f(lambda v: x(x)(v)))(lambda x: f(lambda v: x(x)(v))))(lambda g: lambda n: lambda r: [lambda: not (n - r), lambda: g(n - r)(r)][n - r > 0]())(n)(b)], s[:]][(lambda f: (lambda x: f(lambda v: x(x)(v)))(lambda x: f(lambda v: x(x)(v))))(m)(n)((lambda f: (lambda x: f(lambda v: x(x)(v)))(lambda x: f(lambda v: x(x)(v))))(lambda g: lambda a: lambda b: lambda c: [lambda: c, lambda: g(a - 1)(b)(c + b)][a > 0]())(a)(b)(0))]
# d = lambda g: lambda n: lambda h: [lambda: None, lambda: print((lambda f: (lambda x: f(lambda v: x(x)(v)))(lambda x: f(lambda v: x(x)(v))))(lambda g: lambda n: lambda s: lambda a: lambda b: [[[str(n), s[:4]][(lambda f: (lambda x: f(lambda v: x(x)(v)))(lambda x: f(lambda v: x(x)(v))))(lambda g: lambda n: lambda r: [lambda: not (n - r), lambda: g(n - r)(r)][n - r > 0]())(n)(a)], s[4:]][(lambda f: (lambda x: f(lambda v: x(x)(v)))(lambda x: f(lambda v: x(x)(v))))(lambda g: lambda n: lambda r: [lambda: not (n - r), lambda: g(n - r)(r)][n - r > 0]())(n)(b)], s[:]][(lambda f: (lambda x: f(lambda v: x(x)(v)))(lambda x: f(lambda v: x(x)(v))))(m)(n)((lambda f: (lambda x: f(lambda v: x(x)(v)))(lambda x: f(lambda v: x(x)(v))))(lambda g: lambda a: lambda b: lambda c: [lambda: c, lambda: g(a - 1)(b)(c + b)][a > 0]())(a)(b)(0))])(h + 1)("fizzbuzz")(3)(5)) or g(n)(h + 1)][n - h > 0]()

# hundred = (lambda f: (lambda x: f(lambda v: x(x)(v)))(lambda x: f(lambda v: x(x)(v))))(lambda g: lambda a: lambda b: lambda c: [lambda: c, lambda: g(a - 1)(b)(c + b)][a > 0]())((lambda f: (lambda x: f(lambda v: x(x)(v)))(lambda x: f(lambda v: x(x)(v))))(u)(2)(2)(0))((lambda f: (lambda x: f(lambda v: x(x)(v)))(lambda x: f(lambda v: x(x)(v))))(u)(5)(5)(0))(0)

# (lambda f: (lambda x: f(lambda v: x(x)(v)))(lambda x: f(lambda v: x(x)(v))))(lambda g: lambda n: lambda h: [lambda: None, lambda: print((lambda f: (lambda x: f(lambda v: x(x)(v)))(lambda x: f(lambda v: x(x)(v))))(lambda g: lambda n: lambda s: lambda a: lambda b: [[[n, s[:((lambda f: (lambda x: f(lambda v: x(x)(v)))(lambda x: f(lambda v: x(x)(v))))(lambda g: lambda a: lambda b: lambda c: [lambda: c, lambda: g(a - 1)(b)(c + b)][a > 0]())(2)(2)(0))]][(lambda f: (lambda x: f(lambda v: x(x)(v)))(lambda x: f(lambda v: x(x)(v))))(lambda g: lambda n: lambda r: [lambda: not (n - r), lambda: g(n - r)(r)][n - r > 0]())(n)(a)], s[((lambda f: (lambda x: f(lambda v: x(x)(v)))(lambda x: f(lambda v: x(x)(v))))(lambda g: lambda a: lambda b: lambda c: [lambda: c, lambda: g(a - 1)(b)(c + b)][a > 0]())(2)(2)(0)):]][(lambda f: (lambda x: f(lambda v: x(x)(v)))(lambda x: f(lambda v: x(x)(v))))(lambda g: lambda n: lambda r: [lambda: not (n - r), lambda: g(n - r)(r)][n - r > 0]())(n)(b)], s[:]][(lambda f: (lambda x: f(lambda v: x(x)(v)))(lambda x: f(lambda v: x(x)(v))))(lambda g: lambda n: lambda r: [lambda: not (n - r), lambda: g(n - r)(r)][n - r > 0]())(n)((lambda f: (lambda x: f(lambda v: x(x)(v)))(lambda x: f(lambda v: x(x)(v))))(lambda g: lambda a: lambda b: lambda c: [lambda: c, lambda: g(a - 1)(b)(c + b)][a > 0]())(a)(b)(0))])(h + 1)("fizzbuzz")(3)(5)) or g(n)(h + 1)][n - h > 0]())((lambda f: (lambda x: f(lambda v: x(x)(v)))(lambda x: f(lambda v: x(x)(v))))(lambda g: lambda a: lambda b: lambda c: [lambda: c, lambda: g(a - 1)(b)(c + b)][a > 0]())((lambda f: (lambda x: f(lambda v: x(x)(v)))(lambda x: f(lambda v: x(x)(v))))(lambda g: lambda a: lambda b: lambda c: [lambda: c, lambda: g(a - 1)(b)(c + b)][a > 0]())(2)(2)(0))((lambda f: (lambda x: f(lambda v: x(x)(v)))(lambda x: f(lambda v: x(x)(v))))(lambda g: lambda a: lambda b: lambda c: [lambda: c, lambda: g(a - 1)(b)(c + b)][a > 0]())(5)(5)(0))(0))(0)

hundred = (lambda f: (lambda x: f(lambda v: x(x)(v)))(lambda x: f(lambda v: x(x)(v))))(lambda g: lambda a: lambda b: lambda c: [lambda: c, lambda: g(a - 1)(b)(c + b)][a > 0]())((lambda f: (lambda x: f(lambda v: x(x)(v)))(lambda x: f(lambda v: x(x)(v))))(lambda g: lambda a: lambda b: lambda c: [lambda: c, lambda: g(a - 1)(b)(c + b)][a > 0]())(2)(2)(0))((lambda f: (lambda x: f(lambda v: x(x)(v)))(lambda x: f(lambda v: x(x)(v))))(lambda g: lambda a: lambda b: lambda c: [lambda: c, lambda: g(a - 1)(b)(c + b)][a > 0]())(5)(5)(0))(0)
print((lambda f: (lambda x: f(lambda v: x(x)(v)))(lambda x: f(lambda v: x(x)(v))))(lambda g: lambda a: lambda b: lambda c: [lambda: c, lambda: g(a - 1)(b)(c + b)][a > 0]())((lambda f: (lambda x: f(lambda v: x(x)(v)))(lambda x: f(lambda v: x(x)(v))))(lambda g: lambda a: lambda b: lambda c: [lambda: c, lambda: g(a - 1)(b)(c + b)][a > 0]())(2)(2)(0))((lambda f: (lambda x: f(lambda v: x(x)(v)))(lambda x: f(lambda v: x(x)(v))))(lambda g: lambda a: lambda b: lambda c: [lambda: c, lambda: g(a - 1)(b)(c + b)][a > 0]())(5)(5)(0))(0))

# (lambda f: (lambda x: f(lambda v: x(x)(v)))(lambda x: f(lambda v: x(x)(v))))(lambda g: lambda n: lambda h: [lambda: None, lambda: print((lambda f: (lambda x: f(lambda v: x(x)(v)))(lambda x: f(lambda v: x(x)(v))))(lambda g: lambda n: [[[str(n), "fizz"][(lambda f: (lambda x: f(lambda v: x(x)(v)))(lambda x: f(lambda v: x(x)(v))))(lambda g: lambda n: lambda r: [lambda: not (n - r), lambda: g(n - r)(r)][n - r > 0]())(n)(3)], "buzz"][(lambda f: (lambda x: f(lambda v: x(x)(v)))(lambda x: f(lambda v: x(x)(v))))(lambda g: lambda n: lambda r: [lambda: not (n - r), lambda: g(n - r)(r)][n - r > 0]())(n)(5)], "fizzbuzz"][(lambda f: (lambda x: f(lambda v: x(x)(v)))(lambda x: f(lambda v: x(x)(v))))(lambda g: lambda n: lambda r: [lambda: not (n - r), lambda: g(n - r)(r)][n - r > 0]())(n)(15)])(h + 1)) or g(n)(h + 1)][bool(n - h)]())(100)(0)