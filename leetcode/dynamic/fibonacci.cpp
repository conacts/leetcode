int fib(int n) {
	if (n < 2) { 
		return n;
	}
	int s = 0;
	int a = 0;
	int b = 1;
	n --;
	while (n) {
		s = a + b;
		a = b;
		b = s;
		n --;
	}
	return s;
}
