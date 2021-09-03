#include <bits/stdc++.h>
using namespace std;
ios::sync_with_stdio(0);
cin.tie(0);

int main() {
	return 0;
}

int notes() {
	typedef double d;
	// reads a file as input
	freopen("input.txt", "r", stdin);
	// saves output to file
	freopen("output.txt", "w", stdout);
	// int = 32 bit
	// long long int = 64 bit
	int a, b;
	scanf("%d, %d", &a, &b);
	printf("%d %d \n", a, b);
	strings;
	// grabs entire line with spaces
	getline(cin, s);
	// if amount of data is unknown, this grabs until there is no more
	//while (cin >> x) {}
	
	// c++ has lots of rounding errors, to avoid this use
	if (abs(a-b) < 1e-9) {
	// a and b are equal
	}

}

int moduloFactorial() {
	long long x = 1;
	for (int i = 2; i <=n; i++) {
		x = (x*i)%m;
	}
	cout << x%m << "\n";
