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

	//2. ����Ʈ ī�䰡 ���ִ� ������ �� ���� ���� N�� 4 �̻� 20 ������ �����̴�. (4 �� N �� 20)
	//3. ����Ʈ ������ ��Ÿ���� ���� 1 �̻� 100 ������ �����̴�.
	//���� ���� ���� �� �ִ� ����Ʈ�� ���� ����

	tuple<int, int, int> temp = mystack.back();
	int y = get<0>(temp);
	int x = get<1>(temp);
	int d = get<2>(temp);
	//visited[y][x] = true;

	//ù° ������ ��
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
	//ó�� �ڸ��� ���ƿ����� vector ���� ����ϱ�
	if (mystack.size() != 1) {
		if ((y == start_y) && (x == start_x)) {
			//sum�� ��
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
					if ((p == -1) || (p == n) || (q == -1) || (q == n)) // ���� ��
						continue;
					if (d == 4) //���� �� �ִ� ���Ѻ��� �� ���� �������� �� ��
						continue;
					if ((dessert[data[q][p]] == true) && !((q == start_y) && (p == start_x))) // �̹� ���� ����Ʈ�� �� (�湮���� �ʾҾ ) 
						continue;
					//if ((dessert[data[q][p]] == true)){
						//if (data[q][p] == 49);
						//ontinue;
					//}

					if (visited[q][p] == true && !(q == start_y && p == start_x)) { // �̹� �湮�� ���� ��
						continue;
					}
					
					flag = true;
					mystack.push_back(make_tuple(q, p, d + i));
					dessert[data[q][p]] = true;
					visited[q][p] = true;
					dfs(mystack, data, visited);
					if (!(q == start_y && p == start_x)) dessert[data[q][p]] = false;
					//�ߺ��Ǵ°� �����鼭 dessert�� �ǵ帮�� �ʵ��� �ϴ� ���?
					if (!(q == start_y && p == start_x)) visited[q][p] = false;
					mystack.pop_back();

				
			}
		

	//��� �� �� ������ ����
	//�ٽ� ��������� ���ƿ��� ��츸 ����
	//���°� �� ���� ����
	//���� Ƚ�� ����
	
}