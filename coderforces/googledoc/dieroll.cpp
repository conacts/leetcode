#include <bits/stdc++.h>
using namespace std;

int main() {
	int a, b;
	cin >> a >> b;
	if (a < b) {
		a = b;
	}
	int diff = 7-a;
	if (diff == 6) {
		printf("1/1");
	}
	else if (diff % 2 == 0) {
		printf("%d/%d", diff/2, 6/2);
	}
	else if (diff % 3 == 0) {
		printf("%d/%d", diff/3, 6/3);
	} else {
		printf("%d/%d", diff, 6);
	}
	return 0;
}
