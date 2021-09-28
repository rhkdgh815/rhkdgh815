#include <iostream>
#include <cstring>
using namespace std;

int main() {
	int count = 0;
	char password[11];
	cout << "프로그램을 종료하려면 암호를 입력하세요." << endl;
	while (true) {
		cout << "암호:>>";
		cin >> password;
		if (strcmp(password, "computerl") == 0) {
			cout << "프로그램을 정상 종료합니다." << endl;
			break;
		}
		else
			cout << "암호가틀립니다~!!~" << endl;
		count++;
		if (count == 3) {
			cout << "암호3회이상 틀렸어요 종료합니다." << endl;

			break;
		}
	}
}

	
	


