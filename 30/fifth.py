import math

POWER = 4

def sumOfDigitsToPower(n, p):
  digits = str(n)
  sum = 0
  for i in range(0, len(digits)):
    sum += math.pow(int(digits[i]),p)
  if (sum == n):
    return 1
  return 0

def compute(n):
  numDigits = 1
  # compute upperBound
  upperBound = math.pow(9,5) 
  sum = 0

  if (sumOfDigitsToPower(1634,4)):
    print "True!"

if __name__ == '__main__':
  print compute(POWER)