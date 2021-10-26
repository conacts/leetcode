#include <bits/stdc++.h>
using namespace std;

int main() {
	auto a = bitset<4>(11);
	auto b = bitset<4>(7);
	cout << (a & b) << endl << typeid(a).name() << endl;
	return 0;
}
