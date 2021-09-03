#include <bits/stdc++.h>
using namespace std;

int main() {
	string s, s2 = ""; 
	int upper = 0, lower = 0;
	getline(cin, s);
	for (char c : s) {
		if (isupper(c)) {upper++;}
		else {lower++;}
	}
	if (lower >= upper) {
		for (char c : s) {
			s2.push_back(tolower(c));
		}
	} else {
		for (char c : s) {
			s2.push_back(toupper(c));
		}
	}
	cout << s2;
	return 0;
}
