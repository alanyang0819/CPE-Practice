#include<iostream>
#include<string>
using namespace std;

bool IsEleven(string num) {
  int odd = 0;
  int even = 0;
  for (int i = 0; i < num.length(); i++) {
    if ((i + 1) % 2 == 1) {
      odd += num[i] - 48;
    }
    else {
      even += num[i] - 48;
    }
  }
  if (abs(odd - even) % 11 == 0 ) {
    return true;
  }
  return false;
}

int main() {
  string num;
  cin >> num;
  while (num != "0") {
    if (IsEleven(num)) {
      cout << num << " is a multiple of 11." << endl;
    }
    else {
      cout << num << " is not a multiple of 11." << endl;
    }
    cin >> num;
  }
}