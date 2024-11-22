#include<iostream>
using namespace std;

int ThreeNPlusOne(int num, int length=1) {
 if (num == 1) {
  return length;
 }

 else if (num % 2 == 1) {
  return ThreeNPlusOne(num*3+1, ++length);
 }

 else {
  return ThreeNPlusOne(num/2, ++length);
 }
}

int main() {
  int i, j;
  int result;
  while (cin >> i >> j) {
    int max = 0;
    cout << i << " " << j << " ";
    if (i > j) {
      swap(i, j);
    }
    for (int n = i; n <= j; n++) {
      result = ThreeNPlusOne(n, 1);
      if (result > max) {
        max = result;
      }
    }
    cout << max << endl;
  }
}