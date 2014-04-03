#include <stdio.h>
#include <iostream>
#include <vector>
#include <map>

#define upperBound 28123

using namespace std;

struct number {
  bool isAbundant;
};

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

bool isAbundant(int a) {
  if (sumFactors(a) > a) {
    return true;
  }
  return false;
}

int main(){

  vector<int> abundantNumbers;
  vector<int>::iterator it = abundantNumbers.begin();

  map<int,bool> m;
  
  unsigned long sum = 0;

  for (int i = 1; i <= upperBound; ++i) {
    // for each number from 1 to upperBound, check if it is expressable and abundant

    // check if expressable
    bool expressable = false;
    it = abundantNumbers.begin();
    for ( it=abundantNumbers.begin(); it<abundantNumbers.end(); it++) {
      int a = *it;
      int b = i - a;
      map<int,bool>::iterator it2 = m.find(b);
      if(it2 != m.end())
      {
        // is abundant, both abundant, so i is expressable
        expressable = true;
        break;
      }
    }

    // check if number is abundant
    if (isAbundant(i)) {
      it = abundantNumbers.end();
      it = abundantNumbers.insert(it,i);
      
      m.insert(pair<int,bool>(i,true));
      //printf("Abundant: %d\n", i);
    }

    if (!expressable) {
      printf("Not expressable: %d\n", i);
      sum = sum + i;
    }
  }

  printf("sum is: %lu\n", sum);
  return 0;
}