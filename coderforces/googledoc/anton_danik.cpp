#include <bits/stdc++.h>
using namespace std;

int main() {
	int n, a=0, d=0;
	char k;
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> k;
		if (k == 'A') {
			a++;
		}
		if (k == 'D') {
			d++;
		}
	}
	if (a > d) {
		cout << "Anton";
	} else if (d > a) {
		cout << "Danik";
	} else {
		cout << "Friendship";
	}
	return 0;
}
