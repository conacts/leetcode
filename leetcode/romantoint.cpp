#include <bits/stdc++.h>
using namespace std;
int main() {
	string s = "MCMXCIV"; 
	string x = "IVXLCDM"; 
	int ans = 0, num = 1, slen = s.length();
	int n;
	bool dd = false;
	map<char, int> roman; 
	for (char c : x) {
		roman.insert(pair<char, int>(c, num));	
		if (dd == true) {
			num*=2;
			dd = false;
		} else {
			num*=5;
			dd = true;
		}
	}
	num = 0;
	for (int i = slen-1; i >= 0; i--) {
		n = roman[s.at(i)];
		if (num >  n) {
			ans -= n;
		} else {
			ans += n;
		}
		num = n;
	}
	cout << ans;

}