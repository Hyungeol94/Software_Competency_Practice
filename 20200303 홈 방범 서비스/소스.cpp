#include<stdio.h>
#include<stdlib.h>
#include<iostream>
#include<vector>
#include<string.h>
#include<math.h>

using namespace std;
void calculate();
void compute(int p, int q);
int n, m;
int answer =0;
int** matrix;

int main() {
	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {
		printf("#%d ", i + 1);
		calculate();
	}

}

void calculate() {
	cin >> n >> m;
	matrix = new int*[n];
	for (int i = 0; i < n; i++) {
		matrix[i] = new int[n];
		for (int j = 0; j < n; j++)
			cin >> matrix[i][j];
	}

	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			compute(i, j);
	//compute(3, 3);

	printf("%d\n", answer);
	answer = 0;
}


void compute(int p, int q) {
	//k사이즈를 늘려 가면서 count하기
	//어떻게 움직여야 할까
	//바깥 테두리만 계산해서 더해가는 식으로 해야 한다.
	int count = 0;

	//int k = 3; // 설정하기
	int k = 0;
	if (matrix[p][q])
		count += m;

	if ((k + 1)*(k + 1) + k * k <= count) {
		if (answer < count / m)
			answer = count / m;
	}

	//int answer;

	for (int k = 1; k < 2*n; k++) {
		//반바퀴 돌기

		int j = -k;
		for (int i = -k; i <= k; i++) {
			//for (int j = -k; j <= k; j++) {
				int y = i + p;
				int x = k - abs(j) + q;

				if (y < 0 || y>n - 1 || x < 0 || x>n - 1) {
					j++;
					continue;
				}

				if (matrix[y][x])
					count += m;
			//}
				j++;
		}

		//나머지 반바퀴 돌기
		j = k - 1;
		for (int i = k - 1; i >= -k + 1; i--) {
			//for (int j = k - 1; j >= -k + 1; j--) {
				int y = i + p;
				int x = abs(j) -k + q;

				if (y < 0 || y>n - 1 || x < 0 || x>n - 1) {
					j--;
					continue;
				}

				if (matrix[y][x])
					count += m;
				j--;
			//}
		}

		if ((k + 1)*(k + 1) + k*k <= count) {
			if (answer < count / m)
				answer = count/m;
		}
	}

}