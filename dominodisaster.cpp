#include <bits/stdc++.h>
using namespace std;

int main() {
	int t, n;
	char s, out;
	vector <char> v;
	cin >> t;
	for (int z = 0; z < t; z++) {
		cin >> n;
		for (int i = 0; i < n; i++) {
			cin >> s;
			v.push_back(s);
		}
		for (int a = 0; a < n; a++) {
			if (v.at(a) == 'U') {
				v.insert(v.begin() + a, 'D');
				v.push_back(a-1);
			}
			else if (v.at(a) == 'D') {
				v.insert(v.begin() + a, 'U');
				v.push_back(a-1);
			}
		}
		for (int i = 0; i < v.size(); i++) {
			cout << v.back();
			v.pop_back();
		}
		cout << "\n";
		}
	return 0;
}
