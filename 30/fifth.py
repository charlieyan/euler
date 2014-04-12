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
  lowerBound = 1
  s = 0

  # compute upperBound
  maxSum = numDigits*math.pow(9,n)
  maxRepresentable = int(numDigits * "9")

  while (maxRepresentable <= maxSum):
    # iterate through 
    for i in range(lowerBound,int(maxRepresentable)+1):
      if (sumOfDigitsToPower(i,n) and i != 1):
        s = s + i
        print "found: " + str(i)

    # update number of digits
    numDigits = numDigits + 1

    # update lowerBound
    lowerBound = maxRepresentable

    # update maxSum and maxRepresentable
    maxSum = numDigits*math.pow(9,n)
    maxRepresentable = int(numDigits * "9")

  # one last iteration
  for i in range(lowerBound,int(maxRepresentable)+1):
    if (sumOfDigitsToPower(i,n) and i != 1):
      s = s + i
      print "found: " + str(i)


  return s

if __name__ == '__main__':
  print compute(POWER)