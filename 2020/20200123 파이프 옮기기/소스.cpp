#include<stdio.h>
#include<stdlib.h>
#include<vector>
#include<tuple>
#include<iostream>
using namespace std;
void dfs(int** data, bool** visited);
int n =0;
int cnt = 0;
vector<tuple<int, int, int > > mystack;
//0은 가로, 1은 세로, 2는 대각선
int dx[] = { 1,0,1};
int dy[] = { 0,1,1};

int main() {
	cin >> n;
	//벽도 있다.
	int** data = (int**)malloc(sizeof(int*)*n);
	bool** visited = (bool**)malloc(sizeof(bool*)*n);
	for (int i = 0; i < n; i++) {
		data[i] = (int*)malloc(sizeof(int)*n);
		visited[i] = (bool*)malloc(sizeof(bool)*n);
		for (int j = 0; j < n; j++)
			scanf_s("%d", &data[i][j]);
	}
	mystack.push_back(make_tuple(0, 1, 0));
	visited[0][0] = true;
	visited[0][1] = true;
	dfs(data, visited);
	printf("%d", cnt);
}

void dfs(int** data, bool** visited) {
	//0은 가로, 1은 세로, 2는 대각선
	tuple<int, int, int> temp = mystack.at(mystack.size()-1);
	int y = get<0>(temp);
	int x = get<1>(temp);
	int d = get<2>(temp);

	if (y == n-1 && x == n-1)
		cnt++;

	else
	{
		for (int i = 0; i < 3; i++) {
			if (y + dy[i] == n || x + dx[i] == n)
				continue;
			if (data[y + dy[i]][x + dx[i]] == 1)
				continue;
			if (visited[y + dy[i]][x + dx[i]] == true)
				continue;
			
			if (d == 0) 
				if (i == 1)
					continue;
			
			if (d == 1)
				if (i == 0)
					continue;
			bool flag = false;
			if (i == 2)
				for (int j = 0; j < 3; j++) {
					if (y + dy[j] == n || x + dx[j] == n)
						continue;
					if (data[y + dy[j]][x + dx[j]] == 1)
						flag = true;
				}
			if (flag == true)
				continue;

			visited[y][x] = true;
			mystack.push_back(make_tuple(y + dy[i], x + dx[i], i));
			dfs(data, visited);
			mystack.pop_back();
			visited[y][x] = false;
		}
	}
}