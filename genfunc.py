def genfuncacc(levels, origlevel):
  if levels == 0:
    return origlevel
  else:
    return lambda: genfuncacc(levels - 1, origlevel)

def genfunc(levels):
  return genfuncacc(levels, levels)

def main():
  levels = 200
  test = genfunc(levels)
  print(test()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()())

if __name__ == "__main__":
  main()