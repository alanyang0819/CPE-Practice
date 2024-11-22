#include<iostream>
#include<string>
using namespace std;

int fib(int num) {
  if (num <= 1) {
    return num;
  }
  else {
    return fib(num - 1) + fib(num - 2);
  }
}

int main() {
  int testcases;
  cin >> testcases;
  for (int i = 0; i < testcases; i++) {
    int num;
    string binary = "";
    cin >> num;
    int fib_num = fib(num);
    while (fib_num > 0) {
      int digit = fib_num % 2;
      binary = to_string(digit) + binary;
      fib_num = fib_num / 2;
    }
    cout << num << " = " << binary << " (fib)" << endl;
  }
}