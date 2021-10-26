#include <bits/stdc++.h>
using namespace std;

int main() {
	int n;
	double out = 0;
	cin >> n;
	while (n) {
		out += 1.0/n;
		n--;
	}
	printf("%.12lf\n", out);
	return 0;
}
