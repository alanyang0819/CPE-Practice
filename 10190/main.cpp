#include<iostream>
#include<vector>
using namespace std;

int main() {
  vector<int> num;
  bool boring = false;
  int num_one, num_two;
  cin >> num_one >> num_two;
  num.push_back(num_one);
  while (num_one > 1) {
    if (num_one % num_two == 0) {
      num.push_back(num_one / num_two);
      num_one /= num_two;
    }
    else {
      boring = true;
      cout << "Boring!" << endl;
      return 0;
    }
  }
  for (size_t i = 0; i < num.size(); i++) {
    cout << num[i] << " ";
  }
  cout << endl;
  return 0;
}