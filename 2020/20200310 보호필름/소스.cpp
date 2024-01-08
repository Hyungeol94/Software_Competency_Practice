#include<stdio.h>
#include<stdlib.h>
#include<vector>
#include<iostream>
#include<queue>
#include<string.h>
#include<algorithm>

using namespace std;

void calculate();
int d, w, standard;
int** matrix;
int ** buffer;
int* checklist;
bool* flag;
vector<int> mystack;
vector<int> myvector;
vector<int> drug_vector;
bool found;
bool* visited;

void dfs(int depth);
bool check();
void test();
void test_dfs(int k, int depth, int index);
void drug_treat_dfs(int k, int depth);

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {
		printf("#%d ", i + 1);
		calculate();
		printf("\n");
	}

}

void calculate() {
	//검사기준 k
	cin >> d >> w >> standard;
	found = false;

	matrix = new int*[d];
	buffer = new int*[d];
	visited = new bool[d];
	memset(visited, false, sizeof(bool)*d);
	checklist = new int[standard];
	flag = new bool[w];

	for (int i = 0; i < d; i++) {
		matrix[i] = new int[w];
		buffer[i] = new int[w];
		for (int j = 0; j < w; j++) {
			cin >> matrix[i][j];
			buffer[i][j] = matrix[i][j];
		}

	}

	test();

}



//성능검사
bool check() {
	//standard개 이상 연속되는지 확인하기
	//standard개에 대한 배열을 저장하기
	//int* checklist = new int[standard];
	//bool* flag = new bool[w];
	memset(flag, false, sizeof(bool)*w);

	for (int j = 0; j < w; j++) {
		for (int i = 0; i < d - (standard - 1); i++) {

			bool temp_flag = true;
			for (int t = 0; t < standard - 1 && temp_flag; t++) {
				if (buffer[t + i][j] != buffer[t + i + 1][j]) temp_flag = false;
			}

			if (temp_flag == true)
				flag[j] = true;
		}
		if (flag[j] == false)
			return false;
	}

	return true;
}


void test() {
	for (int i = 0; i <= d && !found; i++) {
		test_dfs(i, 0, 0);
	}
}

void test_dfs(int k, int depth, int index) {
	if (depth == k) {
		drug_treat_dfs(k, 0);
	}
	else {
		for (int i = index; i < d && !found; i++) {
			if (!visited[i]) {
				myvector.push_back(i);
				visited[i] = true;
				test_dfs(k, depth + 1, i + 1);
				myvector.pop_back();
				visited[i] = false;
			}
		}
	}


}

void drug_treat_dfs(int k, int depth) {
	//여기는 myvector를 이용하는 거야
	if (depth == k && !found) {
///////////////////////////////////////////////////////////////////////////////////////
		int i = 0;
		for (int j = 0; j < d; j++) {
			if (i < myvector.size() && myvector.at(i) == j) { //T일 때
				int temp = drug_vector.at(i);
				fill(buffer[j], buffer[j] + w, temp);
				memset(buffer[j], temp, sizeof(int)*w);
				i++;
			}
		}


		if (check() == true) {
			printf("%d", myvector.size());
			found = true;
			return;
		}

		i = 0;
		for (int j = 0; j < d; j++) {
			if (i < myvector.size() && myvector.at(i) == j) {
				for (int c = 0; c < w; c++) {
					buffer[j][c] = matrix[j][c];
				};
				i++;

			}
		}

/////////////////////////////////////////////////////////////////////////////////////////////////
	}

	else {
		for (int i = 0; i < 2 && !found; i++) {
			drug_vector.push_back(i);
			drug_treat_dfs(k, depth + 1);
			drug_vector.pop_back();
		}
	}

}