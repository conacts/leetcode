int climbStairs(int n) {
	if (n < 4) {
		return n;
	}
	int a, b, s;
	s = 0;
	a = 1; 
	b = 2;
	n = n - 2;
	while (n) {
		s = a + b;
		a = b;
		b = s;
		n--;
	}
	return s;
}
