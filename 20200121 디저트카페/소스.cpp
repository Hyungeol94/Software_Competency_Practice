#include<stdio.h>
#include<stdlib.h>
#include<queue>
#include<vector>
#include<tuple>
#include<iostream>

using namespace std;
void dfs(vector<tuple<int, int, int> > mystack, int** data, bool** visited);
bool dessert[101];
bool debug = false;
int dy[] = { -1, 1, 1, -1 };
int dx[] = { 1, 1, -1, -1 };
bool flag = false;
int n;
int sum;

int main() {
	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {
		//scanf("%d", n);
		cin >> n;
		int** data = (int**)malloc(sizeof(int*)*n);
		bool** visited = (bool**)malloc(sizeof(bool*)*n);
		for (int j = 0; j < n; j++) {
			data[j] = (int*)malloc(sizeof(int)*n);
			visited[j] = (bool*)malloc(sizeof(bool)*n);
			for (int k = 0; k < n; k++) {
				//scanf("%d", &data[i][j]);
				cin >> data[j][k];
				visited[j][k] = false;
			}
				
		}

		sum = 0;
		for (int j = 0; j < 101; j++)
			dessert[j] = false;

		flag = false;
		vector<tuple<int, int, int> > mystack;


		//mystack.push_back(make_tuple(1, 0, 0));
		//visited[1][0] = true;
		//dessert[i] = false;
		//dfs(mystack, data, visited);
		for (int j = 1; j < n-1; j++) {
			for (int k = 0; k < n - 2; k++) {
				mystack.push_back(make_tuple(j, k, 0));
				visited[j][k] = true;
				dessert[data[j][k]] = true;
				dfs(mystack, data, visited);
				mystack.clear();
				visited[j][k] = false;
				dessert[data[j][k]] = false;
			}
		}

		if (sum != 0)
			printf("#%d %d\n",i+1, sum);
		else
			printf("#%d %d\n",i+1, -1);
	}
}

void dfs(vector<tuple<int, int, int> > mystack, int** data, bool** visited) {

	//2. 디저트 카페가 모여있는 지역의 한 변의 길이 N은 4 이상 20 이하의 정수이다. (4 ≤ N ≤ 20)
	//3. 디저트 종류를 나타나는 수는 1 이상 100 이하의 정수이다.
	//가장 많이 먹을 수 있는 디저트의 개수 세기

	tuple<int, int, int> temp = mystack.back();
	int y = get<0>(temp);
	int x = get<1>(temp);
	int d = get<2>(temp);
	//visited[y][x] = true;

	//첫째 지점과 비교
	int start_y = get<0>(mystack.at(0));
	int start_x = get<1>(mystack.at(0));
	if ((start_y == 5) && (start_x == 3)){
		int cnt = 0;
		int  cnt2 = 0;
		for (int j = 0; j < mystack.size(); j++) {
			if (get<2>(mystack.at(j)) == 0) cnt++;
			if (get<2>(mystack.at(j)) == 1) cnt2++;
			if ((cnt == 5))// && (cnt2 == 11))
				debug = true;
			}
	}
	//처음 자리로 돌아왔으면 vector 길이 계산하기
	if (mystack.size() != 1) {
		if ((y == start_y) && (x == start_x)) {
			//sum과 비교
			if (sum < mystack.size()) {
				sum = mystack.size() - 1;
			}
			return;
		}
	}

			for (int i = 0; i < 2; i++) {
				int p = dx[d + i] + x;
				int q = dy[d + i] + y;
					

					bool check = false;
					if (d == 2) {
						int cnt = 0;
						int cnt2 = 0;
						for (int j = 0; j < mystack.size(); j++) {
							if (get<2>(mystack.at(j)) == 0) cnt++;
							if (get<2>(mystack.at(j)) == 2) cnt2++;
							if (cnt2 > cnt - 1) {
								check = true;
								break;
							}
						}

						if (check == true) {
							return;
						}
						/*if (check == false)
							if (i == 1)
								continue;*/
					
					}
					

					if ((d == 3) && (i == 1))
						continue;
					if ((p == -1) || (p == n) || (q == -1) || (q == n)) // 벽일 때
						continue;
					if (d == 4) //꺽을 수 있는 제한보다 더 많이 꺽으려고 할 때
						continue;
					if ((dessert[data[q][p]] == true) && !((q == start_y) && (p == start_x))) // 이미 먹은 디저트일 때 (방문하지 않았어도 ) 
						continue;
					//if ((dessert[data[q][p]] == true)){
						//if (data[q][p] == 49);
						//ontinue;
					//}

					if (visited[q][p] == true && !(q == start_y && p == start_x)) { // 이미 방문한 곳일 때
						continue;
					}
					
					flag = true;
					mystack.push_back(make_tuple(q, p, d + i));
					dessert[data[q][p]] = true;
					visited[q][p] = true;
					dfs(mystack, data, visited);
					if (!(q == start_y && p == start_x)) dessert[data[q][p]] = false;
					//중복되는게 빠지면서 dessert를 건드리지 않도록 하는 방법?
					if (!(q == start_y && p == start_x)) visited[q][p] = false;
					mystack.pop_back();

				
			}
		

	//계속 갈 수 있을지 결정
	//다시 출발점으로 돌아오는 경우만 가능
	//꺽는건 세 번만 가능
	//꺽은 횟수 저장
	
}