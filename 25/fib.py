import math

NUMDIGITS = 1000

def numDigits2(n):
  s = str(n)
  return len(s)

def getDigits(n):
  a = 1
  b = 1
  a_place = 1
  while ( numDigits2(a) < n):
    c = a + b
    a = b
    b = c
    a_place = a_place + 1
  return a_place

if __name__ == '__main__':
  print getDigits(NUMDIGITS)
