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
	//k는 몇번 둘릴 것이냐임
	int k;
	cin >> k;

	for (int i = 0; i < 4; i++)
		for (int j = 0; j < 8; j++)
			cin >> sawtooth[i][j];

	//N극이 0으로, S극이 1으로 저장됨

	int saw, dir; 
	//다 끝난 후에 획득하는 점수의 총합을 구하면 되는 거시다.
	
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
		//끝난 다음에 원래대로 되돌려놓기는 어떻게 하지?
	}

	//return sum하면 된다.
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
	//이제 rotate를 쓰면 된다.
	bool check[4];
	for (int i = 0; i < 4; i++)
		check[i] = false;
	check[saw] = true;

	//이거 while문으로 바꿀 수 있을 것 같음
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

	//여기에 붙어있는게 돌아가야 돌아간다는 제약 조건을 추가해야 한다.
	

	int sequence[4];
	if (saw % 2 == 0) { //0과 2라는 말은 첫째와 셋째라는 뜻
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

	//1일 때는 시계 방향
	//-1일 때는 반시계방향
	//줄무늬로 채우기
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