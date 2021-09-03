#include <bits/stdc++.h>
using namespace std;

int main() {
	string s, msg;
	getline(cin, s);
	vector <char> d;
	for (char z : s) {
		if (find(d.begin(), d.end(), z) == d.end()) {
			d.push_back(z);
		}
	}
	if (d.size()%2 == 0) {
		msg = "CHAT WITH HER!"; 
	} else {
		msg = "IGNORE HIM!";
	}
	cout << msg;
	return 0;
}
