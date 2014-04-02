#include <stdio.h>
#include <iostream>
#include <map>

#define upperBound 10000

using namespace std;

int sumFactors(int a) {
  int result = 0;
  int b = a-1;
  while (b > 0) {
    if ((a % b) == 0) {
      result += b;
    }
    b--;
  }
  return result;
}

int findAmicable(int a) {

  // get sum of factors for a
  int target = sumFactors(a);

  // get sum of factors for target
  int targetSum = sumFactors(target);

  return ((targetSum == a) && (target != a)) ? target : 0;
}

int main(){

  bool checked[upperBound] = {false};
  unsigned long sum = 0;

  for (int i = 0; i < upperBound; ++i) {
    // check that it isn't amicable already
    if (!checked[i]) {
      int j = findAmicable(i);
      if (j > 0) {
        // add pair i,j to sum
        sum += i;
        sum += j;
        checked[i] = true;
        checked[j] = true;
      }
    }
  }
  printf("sum is: %lu\n", sum);
  return 0;
}