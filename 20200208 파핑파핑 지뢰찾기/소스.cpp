#include<stdio.h>
#include<stdlib.h>
#include<iostream>
#include<vector>
#include<queue>
#pragma warning(disable:4996)
using namespace std;
//char** matrix;
//bool** visited;
int n;
int t_count = 0;
void calculate(char** matrix, bool** visited);
void check(int r, int c, char** matrix, bool** visited);
bool round(int r, int c, char** matrix, bool** visited);
int dy[] = { -1, -1, -1, 0, 1, 1, 1, 0 };
int dx[] = { -1, 0, 1, 1, 1, 0, -1, -1 };



struct cmp {
	bool operator()(pair<int, int> a, pair<int, int> b) {
		if ((n / 2 - a.first) == abs(n / 2 - b.first))
			return abs(n / 2 - a.second) > abs(n / 2 - b.second);
		return abs(n / 2 - a.first) > abs(n / 2 - b.first);
	}
};

int main() {
	//ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	int t;
	cin >> t;
	char** matrix = (char**)malloc(sizeof(char*)*(301));
	bool** visited = (bool**)malloc(sizeof(bool*)*(301));
	for (int i = 0; i < 301; i++) {
		matrix[i] = (char*)malloc(sizeof(char)*(301));
		visited[i] = (bool*)malloc(sizeof(bool)*(301));
		for (int j = 0; j < (301); j++) {
			visited[i][j] = false;
		}
	}


	for (int i = 0; i < t; i++) {
		printf("#%d ", i + 1);
		calculate(matrix, visited);
		printf("%d\n", t_count);
		//cout << '#' << i + 1 << ' ' << t_count << '\n';
		t_count = 0;
	}

}

void calculate(char** matrix, bool** visited) {
	//ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
	//scanf("%d", &n);
	cin >> n;
	for (int i = 0; i < n; i++) {
		//cin >> matrix[i];
		scanf("%s", matrix[i]);
		for (int j = 0; j < (n + 1); j++) {
			//scanf("%c", &matrix[i][j]);
			visited[i][j] = false;
		}
	}


	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			if (matrix[i][j] == '.') check(i, j, matrix, visited);


	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			if (matrix[i][j] == '.') {
				matrix[i][j] = '*';
				t_count++;
			}

	/*for (int i = 0; i < n; i++) {
		free(visited[i]);
		free(matrix[i]);
	}*/
	//free(visited);
	//free(matrix);

}

void check(int r, int c, char** matrix, bool** visited) {
	if (!round(r, c, matrix, visited)) {
		//bfs ½ÃÀÛ
		queue<pair<int, int> > myqueue;
		myqueue.push(make_pair(r, c));
		visited[r][c] = true;
		matrix[r][c] = '-';
		//matrix[r][c] = '*';
		while (!myqueue.empty()) {
			pair<int, int> temp = myqueue.front();
			myqueue.pop();
			for (int i = 0; i < 8; i++) {
				int y = temp.first + dy[i];
				int x = temp.second + dx[i];
				if (y <= -1 || y >= n)
					continue;
				if (x <= -1 || x >= n)
					continue;
				if (matrix[y][x] == '*')
					continue;
				if (matrix[y][x] == '-')
					continue;
				if (!visited[y][x]) {
					visited[y][x] = true;
					matrix[y][x] = '-';
					//matrix[y][x] = '*';
					if (!round(y, x, matrix, visited))
						myqueue.push(make_pair(y, x));
				}
			}
		}

		/*for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++)
				if (visited[i][j]) matrix[i][j] = '-';
		}*/

		t_count++;
	}
}

bool round(int r, int c, char** matrix, bool** visited) {
	bool flag = false;
	if (matrix[r][c] == '*') flag = true;
	//if (visited[r][c]) flag = true;
	for (int i = 0; i < 8; i++) {
		int y = r + dy[i];
		int x = c + dx[i];
		if (y <= -1 || y >= n)
			continue;
		if (x <= -1 || x >= n)
			continue;
		/*if (visited[y][x])
			continue;*/
		if (matrix[y][x] == '*')
			flag = true;
	}
	return flag;
}