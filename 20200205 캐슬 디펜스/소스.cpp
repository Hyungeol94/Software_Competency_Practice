#include<stdio.h>
#include<stdlib.h>
#include<iostream>
#include<vector>
#include<tuple>
#include<queue>
#include<math.h>

using namespace std;
int n, m, d;
int answer_count = 0;
int kill_count = 0;

queue<pair<int, int> > myqueue;
vector<int> archers;
//pair<int, int> point;


bool location[15];
void dfs(int index, int depth, int** matrix, bool** visited);

struct cmp {
	
	bool operator()(tuple<int, int, int> a, tuple<int, int, int> b) {
		//distance가 같은 경우에는 좌표를 기준으로 판단
		if (get<2>(a) == get<2>(b)) {
			return get<1>(a) > get<1>(b);
		}
		return get<2>(a) > get<2>(b);
	}
};

int main() {
	cin >> n >> m >> d;
	int** matrix = (int**)malloc(sizeof(int*)*(n+1));
	bool** visited = (bool**)malloc(sizeof(bool*)*(n+1));
	for (int i = 0; i < n; i++) {
		matrix[i] = (int*)malloc(sizeof(int)*m);
		visited[i] = (bool*)malloc(sizeof(bool)*m);
		for (int j = 0; j < m; j++) {
			cin >> matrix[i][j];
		}
	}
	matrix[n] = (int*)malloc(sizeof(int)*m);
	visited[n] = (bool*)malloc(sizeof(bool)*m);

	for (int i = 0; i < 15; i++)
		location[i] = false;

	//permute the possible location of the archers
	//각자에게 가장 가까운 적을 계산하기(calculate)
	//answer stack에 push하기
	//1을 0으로 바꾸기. 바꾸면 count++; //count stack에 push하기
	//적들을 한칸씩 밑으로 내리기. 성에 도착하면 지우기
	//적들이 다 사라졌는지 확인하기(clear)
	dfs(0, 0, matrix, visited);
	printf("%d", answer_count);

}

void calculate(int** matrix, bool** visited) {
	//calculate
	
	int** buffer = (int**)malloc(sizeof(int*)*(n + 1));
	for (int i = 0; i < n+1; i++) {
		buffer[i] = (int*)malloc(sizeof(int)*m);
		for (int j = 0; j < m; j++) {
			buffer[i][j] = matrix[i][j];
		}
	}
	
	for (int i = 0; i < 3; i++)
		visited[n][archers.at(i)] = true;
	vector< tuple<int, int, int> > next_target;

	for (int a = 0; a < 3; a++) {
		priority_queue<tuple<int, int, int>, vector<tuple<int, int, int> >, cmp > candidates;
		pair<int, int> point = make_pair(n, archers.at(a)); //n번째 row에 있는 3개의 archers들의 조합
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++)
				if (buffer[i][j] == 1) {
					//priority queue에 push하기
					//거리 계산하기
					int distance = abs(point.first - i) + abs(point.second - j);
					if (distance <= d)
						candidates.push(make_tuple(i, j, distance));
				}
		}


		if (!candidates.empty()) next_target.push_back(candidates.top());
		while (!candidates.empty()) {
			candidates.pop();
		}
	}

	//3개 표적을 다 0으로 바꾸기
	for (int i = 0; i < next_target.size(); i++) {
		tuple<int, int, int> temp = next_target.at(i);
		int y = get<0>(temp);
		int x = get<1>(temp);
		if (buffer[y][x] == 1) {
			buffer[y][x] = 0;
			kill_count++;
		}
	}
	//다 밑으로 내리기
	
	for (int i = 0; i < m; i++) {
		for (int j = n; j > 0; j--) {
			buffer[j][i] = buffer[j - 1][i];
		}
	}
	for (int i = 0; i < m; i++)
		buffer[0][i] = 0;

	//check해서 다 0이면 그만하기
	bool flag = false;
	for (int i = 0; i < m; i++) {
		for (int j = n; j >= 0; j--) {
			if (buffer[j][i] == 1) {
				flag = true;
				break;
			}
		}
	}

	if (flag == false) {
		if (answer_count <= kill_count) answer_count = kill_count;
		kill_count = 0;
		return;
	}
	else return calculate(buffer, visited);
	
}

void dfs(int index, int depth, int** matrix, bool** visited) {
	if (depth == 3) {
		//calculate하기
		//궁수 있는 곳만 마크하기
		for (int i = 0; i < 3; i++)
			location[archers.at(i)] = true;

		//이걸 바탕으로 calculate
		//calculation은 update하는 것
		calculate(matrix, visited);
		
		//location 초기화
		for (int i = 0; i < 15; i++) {
			location[i] = false;
		}
	}

	else {
		for (int i = index; i < m; i++) {
			archers.push_back(i);
			dfs(i + 1, depth + 1, matrix, visited);
			archers.pop_back(); 
		}
	}
}