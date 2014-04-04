import math

NTH = 1000000
MAX = 9

def getPermutation(maxDigit, n):
  answer = ''
  m = n
  list = []
  for i in range(0,maxDigit+1):
    list.append(str(i))

  while (len(list) > 0):
    # start with the first digit
    digit = 0

    # increment is length of list minus digit considered
    increment = math.factorial(len(list)-digit-1)

    # add to upperBound by increment until it meets m
    upperBound = increment
    while (upperBound < m):
      digit = digit + 1
      upperBound = upperBound + increment

    # update answer
    a = list.pop(digit)
    answer = answer + a

    # subtract upperBound reached prior to last increment
    m = m - (upperBound - increment)
  return answer

if __name__ == '__main__':
  print getPermutation(MAX,NTH)
