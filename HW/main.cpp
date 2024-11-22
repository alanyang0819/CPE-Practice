#include<iostream>
#include<cmath>
using namespace std;

int main() {
  int start, end;
  cin >> start >> end;
  while (start != 0 || end != 0) {
    int count = 0;
    for (int i = start; i <= end; i++) {
    int res = sqrt(i);
    if (pow(res, 2) == i) {
      count++;
      }
    }
    cout << count << endl;
    cin >> start >> end;
  }
  return 0;
}