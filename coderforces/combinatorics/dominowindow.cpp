#include <bits/stdc++.h>
using namespace std;

int main() {
	int t, k1, k2, n;
	int w, b;
	vector <string> v;
	cin >> t;
	for (int i = 0; i < t; i++) {
		cin >> n >> k1 >> k2;
		cin >> w >> b;
		if (w*2 <= k1 + k2 && b*2 <= (n*2 - k1 - k2)) {
			v.push_back("YES");
		}
		else {
			v.push_back("NO");
		}
	}
	for (string out : v) {
		cout << out << "\n";
	}
	return 0;
}
