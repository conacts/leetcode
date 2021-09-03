#include <bits/stdc++.h>
using namespace std;

int main() {
	int a, z; 
	cin >> a;
	vector<int> arr;
	for (int i = 0; i < a; i++) {
		cin >> z;
		arr.push_back(z);
	}
	sort(arr.begin(), arr.end());
	for (int i = 0; i < arr.size(); i++) {
		cout << arr[i] << " ";
	}
	return 0;
}
