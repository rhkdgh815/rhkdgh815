#include <iostream>
#include <cstring>
using namespace std;

int main() {
	int count = 0;
	char password[11];
	cout << "���α׷��� �����Ϸ��� ��ȣ�� �Է��ϼ���." << endl;
	while (true) {
		cout << "��ȣ:>>";
		cin >> password;
		if (strcmp(password, "computerl") == 0) {
			cout << "���α׷��� ���� �����մϴ�." << endl;
			break;
		}
		else
			cout << "��ȣ��Ʋ���ϴ�~!!~" << endl;
		count++;
		if (count == 3) {
			cout << "��ȣ3ȸ�̻� Ʋ�Ⱦ�� �����մϴ�." << endl;

			break;
		}
	}
}

	
	


