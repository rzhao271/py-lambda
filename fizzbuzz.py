import sys

def fizzbuzz():
 counter = 1
 max_counter = 101
 def helpme():
  nonlocal counter
  if counter % 3 == 0 and counter % 5 == 0:
   fizzbuzzres = "fizzbuzz"
  elif counter % 3 == 0:
   fizzbuzzres = "fizz"
  elif counter % 5 == 0:
   fizzbuzzres = "buzz"
  else:
   fizzbuzzres = str(counter)
  if counter == max_counter:
   raise Exception("Too many brackets, try again.")
  counter += 1
  print(fizzbuzzres)
  return helpme
 return helpme

fizzbuzz()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()
