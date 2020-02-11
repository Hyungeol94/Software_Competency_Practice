#include<stdio.h>
#include<stdlib.h>
#include<vector>
#include<iostream>
#include<math.h>
#include<algorithm>
#include<set>
#include<queue>
//#pragma warning(disable:4996)

int n, k;
using namespace std;
void calculate();
int* numbers;

struct cmp {
	bool operator()(int a, int b) {
		return a < b;
	}
};

int main() {
	int t = 0;
	cin >> t;
	for (int i = 0; i < t; i++) {
		printf("#%d ", i + 1);
		calculate();
		printf("\n");
	}
	
	
	//system("pause");
	//return 0;
}

void calculate() {
	cin >> n >> k;
	int temp = 0;
	numbers = (int*)malloc(sizeof(int)*n);
	for (int i = 0; i < n; i++) {
		scanf("%1x", &numbers[i]);
	}


	set<int> s = {};
	priority_queue<int, vector<int>, cmp> myqueue;

	for (int i = 0; i < n / 4; i++) {
		rotate(numbers, numbers + n - 1, numbers + n);
		//4���� ���ڰ� ���� ���̴�.
		int j = 0;
		//4�� ���� ���ϱ�
		for(int j =0;j<n;j += n/4){
			int temp = 0; //���� �ϳ� �����
			int c  = pow(16, n/4-1); // ���ڸ� ������ ��� ����?!
			for (int p = j; p < j + n / 4; p++) {
				temp += numbers[p] * c;
				c = c / 16;
			}
			if (s.find(temp) == s.end()) { //set�� �ִٸ� ���� �ʰ�, set�� ���� �ʴٸ� �ֱ�
				s.insert(temp);
				myqueue.push(temp);
			}
		}
	}

	int count = 0;
	temp = 0;
	while (count != k) {
		temp = myqueue.top();
		myqueue.pop();
		//printf("%x ", temp);
		count++;
	}
	printf("%d", temp);

		
	/*for (int i = 0; i < n; i++)
		printf("%x", numbers[i]);*/




}