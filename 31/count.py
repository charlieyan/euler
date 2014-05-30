#Project Euler #31
TOTAL = 200
denominations = [1,2,5,10,20,100,200]

def count(n):
  if (n == 1):
    return 1
  else if (n == 2):
    return 2 #1,1, 2
