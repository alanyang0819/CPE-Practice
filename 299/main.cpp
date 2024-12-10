#include<iostream>
using namespace std;

int main() {
  int testcases;
  cin >> testcases;
  for (int i = 0; i < testcases; i++) {
    int length;
    cin >> length;
    int nums[length];
    for (int i = 0; i < length; i++) {
      cin >> nums[i];
    }
    int swap_count = 0;
    for (int i = 0; i < length; i++) {
      for (int j = 0; j < length - 1; j++) {
        if (nums[j] > nums[j+1]) {
          swap(nums[j], nums[j+1]);
          swap_count++;
        }
      }
    }
    cout << "Optimal train swapping takes " << swap_count << " swaps." << endl;
  }
  return 0;
}