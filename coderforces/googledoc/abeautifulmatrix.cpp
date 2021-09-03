#include <bits/stdc++.h>
using namespace std;

int main() {
	int a, b, c, d, e, m;
	for (int i = 1; i < 6; i++) {
		cin >> a >> b >> c >> d >> e;
		if (a+b+c+d+e > 0) {
			m = abs(3-i);
			i = 6;
		}
	}
	if (a || b) {
		if (a) {m+=2;}
		if (b) {m+=1;}
	}	else if (d || e) {
		if (e) {m+=2;}
		if (d) {m+=1;}
	}
	cout << "\n" << m;
	return 0;
}
