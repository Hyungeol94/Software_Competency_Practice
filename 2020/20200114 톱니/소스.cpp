#include<stdio.h>
#include<stdlib.h>
#include<iostream>
#include<algorithm>

using namespace std;
int sawtooth[4][8];

int calculate();
int spin(int** buffer,int saw, int dir);

int main() {
	int t;
	cin >> t;
	int answer = 0;
	for (int i = 0; i < t; i++) {
		answer = calculate();
		cout << "#"<< i+1 << ' ' << answer << '\n';
	}

	return 0;
}

int calculate() {
	//k�� ��� �Ѹ� ���̳���
	int k;
	cin >> k;

	for (int i = 0; i < 4; i++)
		for (int j = 0; j < 8; j++)
			cin >> sawtooth[i][j];

	//N���� 0����, S���� 1���� �����

	int saw, dir; 
	//�� ���� �Ŀ� ȹ���ϴ� ������ ������ ���ϸ� �Ǵ� �Žô�.
	
	int** buffer = (int**)malloc(sizeof(int*) * 4);
	for (int i = 0; i < 4; i++) {
		buffer[i] = (int*)malloc(sizeof(int) * 8);
		for (int j = 0; j < 8; j++) {
			//buffer[i][i] = 0;
			buffer[i][j] = sawtooth[i][j];
		}
	}

	for (int i = 0; i < k; i++) {	
		cin >> saw >> dir;
		spin(buffer, saw-1, dir);
		//���� ������ ������� �ǵ�������� ��� ����?
	}

	//return sum�ϸ� �ȴ�.
	int sum = 0;

	/*for (int i = 0; i < 4; i++) {
		printf("\n");
		for (int j = 0; j < 8; j++)
			printf("%d", buffer[i][j]);
	}*/

	if (buffer[0][0] == 1) sum++;
	if (buffer[1][0] == 1) sum = sum + 2;
	if (buffer[2][0] == 1) sum = sum + 4;
	if (buffer[3][0] == 1) sum = sum + 8;

	return sum;
}

int spin(int** buffer, int saw, int dir) {
	//���� rotate�� ���� �ȴ�.
	bool check[4];
	for (int i = 0; i < 4; i++)
		check[i] = false;
	check[saw] = true;

	//�̰� while������ �ٲ� �� ���� �� ����
	int temp = saw;
	while (temp != 0) {
		if (buffer[temp][6] != buffer[temp - 1][2]) {
			check[temp - 1] = true;
		}
		else break;
		temp--;
	}

	temp = saw;
	while (temp != 3) {
		if (buffer[temp][2] != buffer[temp + 1][6]) {
			check[temp + 1] = true;
		}
		else break;
		temp++;
	}

	//���⿡ �پ��ִ°� ���ư��� ���ư��ٴ� ���� ������ �߰��ؾ� �Ѵ�.
	

	int sequence[4];
	if (saw % 2 == 0) { //0�� 2��� ���� ù°�� ��°��� ��
		sequence[0] = dir;
		sequence[1] = -dir;
		sequence[2] = dir;
		sequence[3] = -dir;
	}
	else {
		sequence[0] = -dir;
		sequence[1] = dir;
		sequence[2] = -dir;
		sequence[3] = dir;
	}

	//1�� ���� �ð� ����
	//-1�� ���� �ݽð����
	//�ٹ��̷� ä���
	for (int i = 0; i < 4; i++) {
		if (check[i] == true) {
			if (sequence[i] == 1) {
				rotate(buffer[i], buffer[i]+7, buffer[i]+8);
			}
			else
				rotate(buffer[i], buffer[i]+1, buffer[i]+8);
		}
	}

}