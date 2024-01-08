#include<stdio.h>
#include<stdlib.h>
#include<iostream>
#include<vector>
#include<queue>
using namespace std;
int n, w, h;
int sum = 10000;

void run();
void change(int** bricks, bool** visited, pair<int, int> point);
void dfs(int** bricks, bool** visited, int depth);

int main() {
	int t;
	cin >> t;

	for (int i = 0; i < t; i++) {
		sum = 10000;
		run();
		printf("#%d %d\n", i, sum);


	}
}

//좌 우 아래 위
int dy[] = { 0,0,1,-1 };
int dx[] = { -1,1,0,0 };
vector<pair< int, int> > mystack;


void run() {
	//int n, w, h; 전역변수로 선언
	cin >> n >> w >> h;
	int** bricks = (int**)malloc(sizeof(int*)*h);
	bool** visited = (bool**)malloc(sizeof(bool*)*h);
	for (int i = 0; i < h; i++) {
		bricks[i] = (int*)malloc(sizeof(int)*w);
		visited[i] = (bool*)malloc(sizeof(bool)*w);
		for (int j = 0; j < w; j++) {
			cin >> bricks[i][j];
			visited[i][j] = false;
		}
	}

	//visited[1][2] = true;
	//change(bricks, visited, make_pair(1, 2));

	for (int i = 0; i < w; i++) {
		int j = 0;
		while (j != h - 1) {
			if (bricks[j][i] != 0)
				break;
			j++;
		}
		mystack.push_back(make_pair(j, i));
		dfs(bricks, visited, 1);
		mystack.pop_back();
	}


	


	/*for (int i = 0; i < h; i++) {
		printf("\n");
		for (int j = 0; j < w; j++) {
			printf("%2d", bricks[i][j]);
		}
	}

	printf("\n");

	for (int i = 0; i < h; i++) {
		printf("\n");
		for (int j = 0; j < w; j++) {
			printf("%2d", visited[i][j]);
		}
	}*/

	

}
void dfs(int** bricks, bool** visited, int depth) {
	//계속 복사하면서 할 수밖에 없을 것 같은데 메모리 초과가 나지는 않을까 싶다.. 하지만 어쩌겠어
	if (depth == n+1) {
		//남은 bricks의 수를 count해서 update하기
		int count = 0;
		for (int i = 0; i < h; i++) {
			for (int j = 0; j < w; j++) {
				if (bricks[i][j] != 0) count++;
			}
		}
		if (sum >= count) sum = count; // update
	}

	else {
		int** buffer = (int**)malloc(sizeof(int*)*h);
		for (int i = 0; i < h; i++) {
			buffer[i] = (int*)malloc(sizeof(int)*w);
			for (int j = 0; j < w; j++) {
				buffer[i][j] = bricks[i][j];
			}
		}


		pair<int, int> temp = mystack.back();
		//mystack.pop_back();
		change(buffer, visited, temp);

		for (int i = 0; i < w; i++) {
			int j = 0;
			while (j != h - 1) {
				if (buffer[j][i] != 0)
					break;
				j++;
			}
			mystack.push_back(make_pair(j, i));
			dfs(buffer, visited, depth + 1);
			mystack.pop_back();

		}

	}
}

void change(int** bricks, bool** visited, pair<int, int> point) {
	for (int i = 0; i < h; i++)
		for (int j = 0; j < w; j++)
			visited[i][j] = false;

	//bfs 돌리기
	queue<pair<int, int> > myqueue;
	myqueue.push(point);
	while(!myqueue.empty()){
		pair<int, int> temp = myqueue.front();
		myqueue.pop();
		visited[temp.first][temp.second] = true;
		int breadth = bricks[temp.first][temp.second];
		int x, y;
		for (int i = 0; i < 4; i++) { //4방향으로 
			y = temp.first;
			x = temp.second;
			for (int j = 0; j < breadth-1; j++) {//breadth만큼
				y = y + dy[i];
				x = x + dx[i];
				if (y <= -1 || y >= h || x <= -1 || x >= w)
					continue;
				else if (bricks[y][x] == 0)
					continue;
				else if (visited[y][x] == true)
					continue;
				else {
					myqueue.push(make_pair(y, x));
					visited[y][x] = true;
				}
			}
		}
	}

	//없애고 나서 처리를 어떻게 해야 하는가 ..?!
	//다 밑으로 내리기..
	vector<vector<int> > rearrange;

	for (int i = 0; i < w; i++) {
		vector<int> buffer;
		for (int j = h-1; j >= 0; j--) {
			if (!visited[j][i] && bricks[j][i] != 0)
				buffer.push_back(bricks[j][i]);
		}
		rearrange.push_back(buffer);
	}

	//rearrange하기
	for (int i = 0; i < w; i++) {
		vector<int> buffer = rearrange.at(i);
		int index = h - 1;
		for (int j = 0; j < buffer.size(); j++) {
			bricks[index][i] = buffer.at(j);
			index--;
		}
		for (int j = index; j >= 0; j--) {
			bricks[j][i] = 0;
		} //나머지는 다 0으로 채우기
	}

}

