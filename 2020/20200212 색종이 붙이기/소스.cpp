#include<stdio.h>
#include<stdlib.h>
#include<vector>
#include<iostream>
#include<queue>

using namespace std;
int* papers;
int** matrix;
bool** visited;
int n = 10;
int paper_size = 0;
int paper_count = 101;
vector<bool> mystack;
vector<pair<int, int> > points;

bool check(int p, int q, int paper_size);
void calculate();
void bfs();


int main() {
	papers = (int*)malloc(sizeof(int) * 5);
	for (int i = 0; i < 5; i++)
		papers[i] = 5;

	matrix = (int**)malloc(sizeof(int*)*n);
	visited = (bool**)malloc(sizeof(bool*)*n);
	for (int i = 0; i < n; i++) {
		matrix[i] = (int*)malloc(sizeof(int*)*n);
		visited[i] = (bool*)malloc(sizeof(bool*)*n);
		for (int j = 0; j < 10; j++) {
			//scanf("%d", &matrix[i][j]);
			cin >> matrix[i][j];
			visited[i][j] = false;
			if (matrix[i][j] == 1)
				points.push_back(make_pair(i, j));
		}
	}

	for (int i = 0; i < 5; i++)
		papers[i] = 5;

	if (points.size() == 100)
		printf("%d", 4);
	else {
		bfs();

		if (paper_count == 101)
			printf("%d", -1);
		else printf("%d", paper_count);
	}

}

bool check(int p, int q, int paper_size) {

	bool flag = true;
	for (int i = p; i < p + paper_size; i++) {
		for (int j = q; j < q + paper_size; j++) {
			if (i >= n || j >= n) {
				flag = false;
			}
			if (flag == false)
				break;

			if (visited[i][j]) {
				flag = false;
			}


			if (matrix[i][j] == 0) {
				flag = false;
			}

			if (flag == false)
				break;
		}
		if (flag == false)
			break;
	}
	
	return flag;
}


void bfs() {
	if (mystack.size() == points.size()) { // 모든 1들이 다 visited되었다면 count하고 update하는 식으로
		calculate();
	}

	else {
		for (int i = 0; i < 10; i++) {
			for (int j = 0; j < 10; j++) {
				//모두 다 0일 때는 아래 조건을 통과하지 못한다.
				if (matrix[i][j] == 1 && !visited[i][j]) {
					for (int k = 5; k >= 1; k--) {
						if (check(i, j, k) && papers[k-1]!= 0) {
							papers[k - 1] --;
							for (int p = i; p < i + k; p++) {
								for (int q = j; q < j + k; q++) {
									visited[p][q] = true;
									mystack.push_back(k);
								}
							}
							bfs();
							papers[k - 1] ++;
							for (int p = i; p < i + k; p++) {
								for (int q = j; q < j + k; q++) {
									visited[p][q] = false;
									mystack.pop_back();
								}
							}
						}
					}
					return;
				}
			}
		}

	}
};
	
void calculate() {
	int count = 0;
		for (int i = 0; i < 5; i++) {
			count += 5 - papers[i];
		}

		if (paper_count >= count)
			paper_count = count;
}



