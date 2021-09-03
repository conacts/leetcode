#include <bits/stdc++.h>
//#include <iostream>
using namespace std;

int main() {
	int k, h, a, sum = 0;
	cin >> k >> h;
	for (int i = 0; i < k; i++) {
		cin >> a;
		sum++;
		if (a > h) {
			sum++;
		}
	}
	cout << sum;
}
