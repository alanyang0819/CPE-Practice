#include<iostream>
using namespace std;

int main() {
  int testcases;
  cin >> testcases;
  for (int i = 0; i < testcases; i++) {
    int length;
    cin >> length;
    int num[length];
    int swap_count = 0;
    for(int i = 0; i < length; i++) {
      cin >> num[i];
    }
    for (int i = 0; i < length - 1; i++) { 
      for (int j = 0; j < length - i - 1; j++) {
        if (num[j] > num[j+1]) {
        swap(num[j], num[j+1]);
        swap_count++;
        }
      }
    }
    cout << "Optimal train swapping takes " << swap_count << " swaps."<< endl;
  }
}