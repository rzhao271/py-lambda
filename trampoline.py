def trampoline(f, *args):
	'''
	From https://clojure.github.io/clojure/clojure.core-api.html#clojure.core/trampoline
	trampoline can be used to convert algorithms requiring mutual
	recursion without stack consumption.
	'''
	fn = f(*args);
	while callable(fn):
		fn = fn()
	return fn

def factorial(n):
	def fac_acc(cur, acc):
		if cur == 0:
			return lambda: acc
		else:
			return lambda: fac_acc(cur - 1, acc * cur)
	return lambda: fac_acc(n, 1)

print(trampoline(factorial, 50000))

