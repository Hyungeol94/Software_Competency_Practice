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
			return matrix[a_y][a_x] < matrix[b_y][b_x]; // life가 큰 것 먼저 return하기
		else
			return time_past[a_y][a_x] > time_past[b_y][b_x]; // 작은 것 먼저 return하기 ->그래야 공평하게 시간돌아감

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
	//matrix에는 생명력 수치 + 세포의 위치 정보가 있다.
	//이미 셀에 번식해 있는 경우 수치 비교해서 높을 때에만 update하기
	//시간의 흐름대로 흘러가야.. 
	//비활, 활, 사 체크 어떤 식으로?  0,1,2
	//priority_queue사용해서 life 큰것이 먼저 나오도록 해야겠다. 


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

		if (time_count[y][x] > 0) { //아직 활성화될 때가 아닐 때
			time_count[y][x]--;
			time_past[y][x]++;
			myqueue.push(make_pair(y, x));
		}
		else if (time_count[y][x] == 0) { //활성화되는 시점일 때 주변으로 복제
			time_count[y][x]--;

			for (int i = 0; i < 4; i++) {
				int next_y = y + dy[i];
				int next_x = x + dx[i];

				if (visited[next_y][next_x]) // time_past가 같을 때는 life가 큰게 무조건 먼저 나왔을 것!
					continue;
				visited[next_y][next_x] = true;
				time_past[next_y][next_x] = time_past[y][x] + 1;

				if (time_past[next_y][next_x] <= k) { //k시간대까지만 배양한다. 그 이후는 큐에 넣지 않는다. 
					time_count[next_y][next_x] = life;
					matrix[next_y][next_x] = life;
					myqueue.push(make_pair(next_y, next_x));
				}
				/*else {
					if (abs(time_count[y][x]) <= matrix[y][x])
						count++;
				}*/
			}

			// 살아 있을 수 있는 구간이 세포마다 다름
			// 살아있다면 다시 큐에 push
			time_past[y][x]++;
			if (time_past[y][x] <= k) { //아직 시간이 지나지 않았음
				if (abs(time_count[y][x] <= life)) { //아직 살아있음
					myqueue.push(make_pair(y, x));
				}
			}
			/*else {
				if (abs(time_count[y][x]) <= matrix[y][x])
					count++;
			}*/
		}

		else if (time_count[y][x] <= -1) { //활성화 시점이 지난 상태
			time_count[y][x]--;
			time_past[y][x]++;
			if (time_past[y][x] <= k) { //아직 시간이 지나지 않았음
				if (abs(time_count[y][x]) <= life) //아직 살아 있음
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