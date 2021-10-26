#include <bits/stdc++.h>
using namespace std;

int main() {
	int sets, iter;
	cin >> sets;
	for (int i=0; i < sets; i++) {
		cin >> iter;
		double a;
		double max = -9999999999999, sum = 0;
		for (int j = 0; j < iter; j++) {
			cin >> a;
			if (max < a) {max = a;}
			sum += a;	
		}
		sum -= max;
		double avg = sum/double(iter-1);
		cout << max << " " << avg << endl;
		cout << fixed << setprecision(9) << max + avg << endl;
	}
	return 0;
}
