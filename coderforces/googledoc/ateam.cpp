#include <bits/stdc++.h>
using namespace std;

int main() {
	int d, sum = 0;
	cin >> d;
	while (d--) {
		int a, b, c;
		cin >> a >> b >> c;
		if (a+b+c >= 2) {
			sum++;
		}
	}
	cout << sum;
	return 0;
}
