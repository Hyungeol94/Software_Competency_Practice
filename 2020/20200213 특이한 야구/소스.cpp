#include<stdio.h>
#include<stdlib.h>
#include<vector>
#include<iostream>

using namespace std;
int n;
int** matrix;
bool* visited;
vector<int> mystack;
int max_points = 0;
void calculate();
void dfs(int depth);

int main() {
	cin >> n;

	//각 선수가 각 이닝에서 얻는 결과
	matrix = (int**)malloc(sizeof(int*)*n);
	for (int i = 0; i < n; i++) {
		matrix[i] = (int*)malloc(sizeof(int) * 9);
		for (int j = 0; j < 9; j++) {
			cin >> matrix[i][j];
		}
	}
	visited = (bool*)malloc(sizeof(bool) * 9);
	for (int i = 0; i < 9; i++)
		visited[i] = false;

	visited[0] = true;
	dfs(0);
	printf("%d", max_points);
	//system("pause");

}


void dfs(int depth){
	//타순 후보들
	if (depth == 9) {
		calculate();
	}
	else if (depth == 3) {
		mystack.push_back(0);
		dfs(depth + 1);
		mystack.pop_back();
	}
	else {
		for(int i =0;i<9;i++)
			if (!visited[i]) {
				visited[i] = true;
				mystack.push_back(i);
				dfs(depth+1);
				mystack.pop_back();
				visited[i] = false;
			}
	}
}


void calculate() {
	//mystack에는 타순이 들어가 있다.
	//out이 n*3만큼 나오면 계산 종료
	//1점 추가는 연산을 계속 하면서 4이상 나올 때
	
	int i = 0;
	int out_count = 0;
	int points = 0;
	//int location = 0;

	for (int k = 0; k < n; k++) {
		//vector<int> runners;
		int runners[9];
		for (int i = 0; i < 9; i++)
			runners[i] = 0;

		while (1) {
			if (out_count == 3) break;
			int next = mystack.at(i % 9);
			switch (matrix[k][next]) {
			case 0:
				out_count++;
				break;
			case 1:
				for (int j = 0; j < 9; j++)
					if (runners[j] > 0) runners[j]++;
				runners[next]++;
				break;
			case 2:
				for (int j = 0; j < 9; j++)
					if (runners[j] > 0) runners[j] += 2;
				runners[next]+= 2;
				break;
			case 3:
				for (int j = 0; j < 9; j++)
					if (runners[j] > 0) runners[j] +=3;
				runners[next]+= 3;
				break;
			case 4:
				for (int j = 0; j < 9; j++)
					if (runners[j] > 0) runners[j] += 4;
				runners[next]+= 4;
				break;
			}
			/*for (int j = runners.size()-1; j>=0; j--) {
				if (runners.at(j) >= 4) {
					points++;
					runners.pop_back();
				}
			}*/
			for (int j = 0; j < 9; j++) {
				if (runners[j] >= 4) {
					points++;
					runners[j] = 0;
				}
			}
			i++;
		}
		out_count = 0;
	}
	if (points >= max_points)
		max_points = points;

}