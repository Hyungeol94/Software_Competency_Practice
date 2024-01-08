#include<stdio.h>
#include<stdlib.h>
#include<iostream>	
#include<vector>
#include<math.h>

using namespace std;
struct ap {
	int power;
	int radius;
	int x;
	int y;
};

int m, a;
int** matrix;
int* ap_count;
bool* a_candidates;
bool* b_candidates;
vector<ap> aps;
vector<int> mystack;
vector<int> charges_track;
int move_sum = 0;
int point_sum = 0;
void dfs(); 
void compute();
//0 1 2 3 4
//No �� �� �� ��
int dy[] = { 0, -1, 0, 1, 0 };
int dx[] = { 0, 0, 1, 0, -1 };


int main() {
	int t = 0;
	cin >> t;

	/*matrix = (int**)malloc(sizeof(int*) * 10);
	for (int i = 0; i < 10; i++) {
		matrix[i] = (int*)malloc(sizeof(int) * 10);
		for (int j = 0; j < 10; j++)
			matrix[i][j] = 0;
	}
*/

	for (int i = 0; i < t; i++) {
		printf("#%d ", i + 1);
		compute();
		printf("%d\n", move_sum);
		move_sum = 0;
	}


}

void compute() {
	
	// 0,1, 2, 3, 4�� �̵�
	// �����A�� ������ (1, 1) ��������, �����B�� ������ (10, 10) �������� ����Ѵ�
	//m�� movement�� ����, a�� ap�� ����
	vector<pair<int, int> > a_track;
	vector<pair<int, int> > b_track;
	

	cin >> m >> a;
	ap_count = (int*)malloc(sizeof(int)*a);
	a_candidates = (bool*)malloc(sizeof(bool)*a);
	b_candidates = (bool*)malloc(sizeof(bool)*a);
	for (int i = 0; i < a; i++) {
		ap_count[i] = 0;
		a_candidates[i] = false;
		b_candidates[i] = false;
	}

	a_track.push_back(make_pair(0, 0));
	b_track.push_back(make_pair(9, 9));

	for (int i = 0; i < m; i++) {
		pair<int, int> temp = a_track.back();
		int d;
		cin >> d;
		int y = temp.first + dy[d];
		int x = temp.second + dx[d];
		a_track.push_back(make_pair(y, x));
	}

	for (int i = 0; i < m; i++) {
		pair<int, int> temp = b_track.back();
		int d;
		cin >> d;
		int y = temp.first + dy[d];
		int x = temp.second + dx[d];
		b_track.push_back(make_pair(y, x));
	}

	for (int i = 0; i < a; i++) {
		int x, y, radius, power;
		cin >> x >> y >> radius >> power;
		ap temp;
		temp.x = x-1; temp.y = y-1; temp.radius = radius; temp.power = power;
		aps.push_back(temp);
	}

	for (int i = 0; i <= m; i++) {
		//a_track ���
		pair<int, int> a_point = a_track.at(i);
		pair<int, int> b_point = b_track.at(i);
		for (int j = 0; j < a; j++) { //��� ap�鿡 ���ؼ� üũ�� �ϴ� ��
			if (abs(a_point.first - aps.at(j).y) + abs(a_point.second - aps.at(j).x) <= aps.at(j).radius)  //�Ÿ��� ap�� ���Եȴٸ�
				a_candidates[j] = true;
			else
				a_candidates[j] = false;

			if (abs(b_point.first - aps.at(j).y) + abs(b_point.second - aps.at(j).x) <= aps.at(j).radius) //�Ÿ��� ap�� ���Եȴٸ�
				b_candidates[j] = true;
			else
				b_candidates[j] = false;
		}
		
		//���� ��� ������ ���ؼ� calculate�ϱ�
		//������ ��� ������ ���ص� 2*5 = 32���ۿ� ����.
		point_sum = 0;
		dfs();
		move_sum += point_sum;
	}


	//�� ������ aps �ʱ�ȭ
	while (!aps.empty())
		aps.pop_back();
}

void dfs() {
	if (mystack.size() == 2) {
		int temp_sum= 0;
		int first = mystack.at(0);
		int second = mystack.at(1);
		if (a_candidates[first] == true)
			ap_count[first]++;
		if (b_candidates[second] == true)
			ap_count[second]++;

		for (int i = 0; i < a; i++) {
			if (ap_count[i] > 0) {
				temp_sum += aps[i].power / ap_count[i];
			}
		}

		if (temp_sum >= point_sum)
			point_sum = temp_sum;
				
		//�ʱ�ȭ�� �� �־�� �մϴ�.
		//��� �ʱ�ȭ�� �ȵȰɱ� ..
		for (int i = 0; i < a; i++) {
			ap_count[i] = 0;
		}		

	}
	else {
		for (int i = 0; i < a; i++) {
			mystack.push_back(i);
			dfs();
			mystack.pop_back();
		}
	}

}
