import math

seen = {}

ALOW = 2
AHIGH = 100
BLOW = 2
BHIGH = 100

def distinctPowers(l1,h1,l2,h2):
  for a in range(l1, h1+1):
    for b in range(l2, h2+1):      
      seen[math.pow(a,b)] = 1
      seen[math.pow(b,a)] = 1
  return len(seen.keys())

if __name__ == '__main__':
  print distinctPowers(ALOW,AHIGH,BLOW,BHIGH)