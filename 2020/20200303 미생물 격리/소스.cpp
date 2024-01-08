#include<stdio.h>
#include<stdlib.h>
#include<vector>
#include<iostream>
#include<queue>
#include<string.h>

using namespace std;
void calculate();
int n, m, k;
int dy[] = { -1, 1, 0, 0 };
int dx[] = { 0, 0, -1, 1 };

int** matrix;
int** directions;



struct microb {
	int y;
	int x;
	int direction;
	int time_past;
	int energy;
};


struct cmp {
	bool operator() (microb a, microb b) {
		return a.energy < b.energy;
	}
};

priority_queue<microb, vector<microb>, cmp> myqueue;


int main() {
	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {
		printf("#%d ", i + 1);
		calculate();
	}
}

void calculate() {
	cin >> n >> m >> k;



	for (int i = 0; i < k; i++) {
		int y, x, direction, energy;
		cin >> y >> x >> energy>> direction;
		microb temp;
		temp.y = y;
		temp.x = x;
		temp.energy = energy;
		temp.direction = direction;
		temp.time_past = 0;
		myqueue.push(temp);
	}


	int count = 0;
	matrix = new int*[n];
	directions = new int*[n];

	for (int i = 0; i < n; i++) {
		matrix[i] = new int[n];
		directions[i] = new int[n];
	}

	for (int c = 0; c < m; c++) {
		for (int i = 0; i < n; i++) {
			memset(matrix[i], 0, sizeof(int)*n);
			memset(directions[i], 0, sizeof(int)*n);
		}

		//꺼내기 -> 매트릭스에 표시 -> 다시 넣기 ->반복
		while (!myqueue.empty()) {
			//꺼내기
			microb temp = myqueue.top();
			myqueue.pop();
			int y = temp.y;
			int x = temp.x;
			int direction = temp.direction;
			int energy = temp.energy;

			y = y + dy[direction - 1];
			x = x + dx[direction - 1];


			//가장자리로 갔을 때
			if (y == n-1 || y == 0 || x == n-1 || x == 0) {
				//방향 바꾸기
				if (direction % 2 == 0)
					direction--;
				else direction++;

				//반으로 줄이기
				energy /= 2;
			}


			//matrix에 표시하기
			if (matrix[y][x]>=1) {
				matrix[y][x] += energy;
			}

			else {
				matrix[y][x] = energy;
				directions[y][x] = direction;
			}
		}


		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				if (c != m-1) {
					if (matrix[i][j]) {
						microb temp;
						temp.y = i;
						temp.x = j;
						temp.energy = matrix[i][j];
						temp.direction = directions[i][j];
						myqueue.push(temp);
					}
				}
				else 
					if (matrix[i][j]) {
						count += matrix[i][j];
					}
			}
		}
	}

	printf("%d \n", count);

}