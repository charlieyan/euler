NTH = 1001

def sumSpirals(sideWidth):
  sum = 1

  rightNum = 2
  offset = 2
  while (offset + 1 <= sideWidth):
    bottomRight = rightNum + offset / 2
    bottomLeft = bottomRight + offset
    topLeft = bottomLeft + offset
    topRight = topLeft + offset
    sum = sum + bottomRight + bottomLeft + topLeft + topRight
    #update
    rightNum = topRight + 1 + offset / 2
    offset = offset + 2

  return sum

if __name__ == '__main__':
  print sumSpirals(NTH)