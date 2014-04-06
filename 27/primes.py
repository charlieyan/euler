def isPrime(n):
  # negative values are not prime!
  if n < 0:
    return 0
  if (n == 1):
    return 0
  if (n == 2):
    return 1
  for x in range(2, n):
    if n%x == 0:
      return 0
  return 1

def LongestPrime(a,b):
  n = 0
  p = 1
  while (p):
    val = n*n + a*n + b
    p = isPrime(val)
    n += 1
  return n-1

def getCoeffs():
  longestA = -1000
  longestB = -1000
  maxLen = 0
  for a in range(-999,1000):
    for b in range(-999,1000):
      l = LongestPrime(a,b)
      #print str(a) + "," + str(b) + ", len: " + str(l)
      if (l > maxLen):
        longestA = a
        longestB = b
        maxLen = l
  return longestA*longestB

if __name__ == '__main__':
  print getCoeffs()