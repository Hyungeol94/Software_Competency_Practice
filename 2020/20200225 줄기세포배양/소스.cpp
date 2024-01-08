#include<stdio.h>
#include<stdlib.h>
#include<iostream>
#include<queue>
#include<vector>
#include<tuple>
#include<math.h>
#include<string.h>
#define LIMIT 360

using namespace std;
int matrix[LIMIT][LIMIT];
bool visited[LIMIT][LIMIT];
int time_count[LIMIT][LIMIT];
int energy[LIMIT][LIMIT];
int time_past[LIMIT][LIMIT];;

void calculate();
int sum = 0;
int dy[] = { -1,1, 0, 0 };
int dx[] = { 0,0,1,-1 };

struct cmp {
	bool operator()(pair<int, int> a, pair<int, int> b) {
		int a_y = get<0>(a);
		int a_x = get<1>(a);
		int b_y = get<0>(b);
		int b_x = get<1>(b);

		if (time_past[a_y][a_x] == time_past[b_y][b_x])
			return matrix[a_y][a_x] < matrix[b_y][b_x]; // life�� ū �� ���� return�ϱ�
		else
			return time_past[a_y][a_x] > time_past[b_y][b_x]; // ���� �� ���� return�ϱ� ->�׷��� �����ϰ� �ð����ư�

	}
};


int main() {
	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {
		calculate();
		printf("#%d %d\n", i + 1, sum);
	}

	return 0;

}

void calculate() {
	int n, m, k;
	int count = 0;
	cin >> n >> m >> k;
	//matrix���� ����� ��ġ + ������ ��ġ ������ �ִ�.
	//�̹� ���� ������ �ִ� ��� ��ġ ���ؼ� ���� ������ update�ϱ�
	//�ð��� �帧��� �귯����.. 
	//��Ȱ, Ȱ, �� üũ � ������?  0,1,2
	//priority_queue����ؼ� life ū���� ���� �������� �ؾ߰ڴ�. 


	priority_queue<pair<int, int>, vector<pair<int, int> >, cmp >myqueue;

	for (int i = 0; i < LIMIT; i++) {
		/*for (int j = 0; j < LIMIT; j++) {
			matrix[i][j] = 0;
			visited[i][j] = 0;
			time_count[i][j] = -1;
			time_past[i][j] = 0;
		}*/
		memset(matrix[i], 0, sizeof(matrix[i]));
		memset(visited[i], 0, sizeof(visited[i]));
		memset(time_count[i], -1, sizeof(time_count[i]));
		memset(time_past[i], 0, sizeof(time_past[i]));
	}

	for (int i = LIMIT / 2 - n / 2; i < LIMIT / 2 - n / 2 + n; i++) {
		for (int j = LIMIT / 2 - m / 2; j < LIMIT / 2 - m / 2 + m; j++) {
			cin >> matrix[i][j];
			time_past[i][j] = 0;
			if (matrix[i][j] > 0) {
				myqueue.push(make_pair(i, j));
				time_count[i][j] = matrix[i][j];
				visited[i][j] = true;
				time_past[i][j] = 0;
			}
		}
	}

	while (!myqueue.empty()) {
		pair<int, int> temp = myqueue.top();
		myqueue.pop();
		int y = get<0>(temp);
		int x = get<1>(temp);
		int life = matrix[y][x];

		if (time_count[y][x] > 0) { //���� Ȱ��ȭ�� ���� �ƴ� ��
			time_count[y][x]--;
			time_past[y][x]++;
			myqueue.push(make_pair(y, x));
		}
		else if (time_count[y][x] == 0) { //Ȱ��ȭ�Ǵ� ������ �� �ֺ����� ����
			time_count[y][x]--;

			for (int i = 0; i < 4; i++) {
				int next_y = y + dy[i];
				int next_x = x + dx[i];

				if (visited[next_y][next_x]) // time_past�� ���� ���� life�� ū�� ������ ���� ������ ��!
					continue;
				visited[next_y][next_x] = true;
				time_past[next_y][next_x] = time_past[y][x] + 1;

				if (time_past[next_y][next_x] <= k) { //k�ð�������� ����Ѵ�. �� ���Ĵ� ť�� ���� �ʴ´�. 
					time_count[next_y][next_x] = life;
					matrix[next_y][next_x] = life;
					myqueue.push(make_pair(next_y, next_x));
				}
				/*else {
					if (abs(time_count[y][x]) <= matrix[y][x])
						count++;
				}*/
			}

			// ��� ���� �� �ִ� ������ �������� �ٸ�
			// ����ִٸ� �ٽ� ť�� push
			time_past[y][x]++;
			if (time_past[y][x] <= k) { //���� �ð��� ������ �ʾ���
				if (abs(time_count[y][x] <= life)) { //���� �������
					myqueue.push(make_pair(y, x));
				}
			}
			/*else {
				if (abs(time_count[y][x]) <= matrix[y][x])
					count++;
			}*/
		}

		else if (time_count[y][x] <= -1) { //Ȱ��ȭ ������ ���� ����
			time_count[y][x]--;
			time_past[y][x]++;
			if (time_past[y][x] <= k) { //���� �ð��� ������ �ʾ���
				if (abs(time_count[y][x]) <= life) //���� ��� ����
					myqueue.push(make_pair(y, x));
			}
			/*else {
				if (abs(time_count[y][x]) <= matrix[y][x])
					count++;
			}*/
		}
	}



	for (int i = 0; i < LIMIT; i++) {
		for (int j = 0; j < LIMIT; j++) {
			if (abs(time_count[i][j]) <= matrix[i][j])
				count++;
		}
	}

	sum = count;

}