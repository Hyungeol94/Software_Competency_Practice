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
//No 상 우 하 좌
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
	
	// 0,1, 2, 3, 4로 이동
	// 사용자A는 지도의 (1, 1) 지점에서, 사용자B는 지도의 (10, 10) 지점에서 출발한다
	//m은 movement의 갯수, a는 ap의 갯수
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
		//a_track 계산
		pair<int, int> a_point = a_track.at(i);
		pair<int, int> b_point = b_track.at(i);
		for (int j = 0; j < a; j++) { //모든 ap들에 대해서 체크를 하는 것
			if (abs(a_point.first - aps.at(j).y) + abs(a_point.second - aps.at(j).x) <= aps.at(j).radius)  //거리가 ap에 포함된다면
				a_candidates[j] = true;
			else
				a_candidates[j] = false;

			if (abs(b_point.first - aps.at(j).y) + abs(b_point.second - aps.at(j).x) <= aps.at(j).radius) //거리가 ap에 포함된다면
				b_candidates[j] = true;
			else
				b_candidates[j] = false;
		}
		
		//이제 모든 조합을 구해서 calculate하기
		//어차피 모든 조합을 구해도 2*5 = 32개밖에 없다.
		point_sum = 0;
		dfs();
		move_sum += point_sum;
	}


	//다 끝나면 aps 초기화
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
				
		//초기화를 해 주어야 합니다.
		//어디가 초기화가 안된걸까 ..
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
