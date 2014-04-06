import math
from decimal import * 

def detectRepeatLen(s):
  flipped = s[2:][::-1]
  if (len(flipped) < 1000):
    return 0
  chunkSize = 1
  found = 0
  offset = 0
  while (not found):
    while( chunkSize < len(flipped)/2 ):
      piece = flipped[offset:offset+chunkSize]
      nextPiece = flipped[offset+chunkSize:offset+chunkSize*2]
      if (piece == nextPiece):
        return chunkSize
      chunkSize += 1
    offset += 1
    chunkSize = 1
  return chunkSize

def countCycle(n):
  getcontext().prec = 2000
  s = str(Decimal(1)/Decimal(n))
  return detectRepeatLen(s)

if __name__ == '__main__':
  maxLen = 0
  maxD = 0
  for d in range(2,1000):
    if ((d % 2) == 1):
      if (countCycle(d) > maxLen):
        maxLen = countCycle(d)
        maxD = d
  print str(maxD) + " with length " + str(maxLen)