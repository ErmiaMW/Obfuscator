int main() {
	int selector_7271 = 1;

	while (selector_7271 > 0) {
	switch(selector_7271) {
		case 1:
			int a = 3;
			selector_7271 = 2;
			break;
		case 2:
			int b = 5;
			selector_7271 = 3;
			break;
		case 3:
			int g = a + b;
			selector_7271 = 4;
			break;
		case 4:
			printf("%d\n", a + b);
			selector_7271 = 5;
			break;
		case 5:
			return 0;
			selector_7271 = 6;
			break;
		case 6:
			selector_7271 = 0;
			break;
	}
}
}
