#include<iostream>
#include<string>
#include<cmath>
using namespace std;

int main() {
  string num;
  cin >> num;
  int num_sum = 0;
  for (int i = 0; i < num.length(); i++) {
    num_sum += (num[i] - 48) * pow(10, num.length() - 1 - i);  
  }
  int ori = num_sum;
  int sum = 0;
  while (num_sum > 0) {
    int digit = num_sum % 10;
    sum += pow(digit, num.length());
    num_sum /= 10;
  }

  if (ori == sum) {
    cout << "True" << endl;
  }
}