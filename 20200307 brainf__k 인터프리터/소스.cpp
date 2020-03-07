#include<stdio.h>
#include<stdlib.h>
#include<iostream>
#include<vector>
#include<string>
#include<string.h>
#include<math.h>
#pragma warning(disable:4996);

using namespace std;
int m, c, s;
unsigned int* dataset;
char* brainfuck;
int pointer;
int k;
int scancount;
string str;

int count_times;
void calculate();
void execute(char c);
void jump(int location);

int main() {
	int t; 
	cin >> t;
	for (int i = 0; i < t; i++) {
		calculate();
		printf("\n");
	}
	
}

void calculate() {
	scanf("%d", &m);
	scanf("%d", &c);
	scanf("%d", &s);
	//cin >> m >> c >> s;
	
	count_times = 0;
	scancount = 0;
	dataset = new unsigned int[m];
	memset(dataset, 0, m * sizeof(int));
	brainfuck = new char[c];
	pointer = 0;


	cin.ignore(256, '\n');
	for (pointer = 0; pointer < c; pointer++) {
		scanf("%1c", &brainfuck[pointer]);
	}

	cin.ignore(256, '\n');
	cin >> str;

	pointer = 0;
	bool flag = false;
	for (k = 0; k < c && !flag; k++) {
		char command = brainfuck[k];
		execute(command);
		//printf("%d\n", count_times);
		if (count_times > 50000000 && brainfuck[k] == '[') {
				flag = true;
		}

	}


	if (count_times > 50000000) {
		printf("Loops ");
		//pointer = pointer + 1;
		//가장 바깥
		int i = k;
	
		int outer_loop = 0;
		while (i!=-1 && brainfuck[i]!= ']') {
			if (brainfuck[i] == '[') outer_loop++;
			i--;
		}

		if (outer_loop == 0) {
			printf("%d ", k - 1);
			flag = false;
			while (!flag && brainfuck[k] != ']') {
				k++;
			}
			printf("%d", k);
		}

		else {	
			i = k;
			while (outer_loop!=0) {
				if (brainfuck[i] == '[') outer_loop--;
				i--;
			}
			i++;
			printf("%d ", i);

			vector<char> myvector;
			myvector.push_back('[');
			while (!myvector.empty()) {
				i++;
				if (brainfuck[i] == '[')
					myvector.push_back('[');

				else if (brainfuck[i] == ']')
					myvector.pop_back();
			}
			printf("%d", i);


		}

	}

	else
		printf("Terminates");
		
}

void execute(char c) {
	count_times++;
	switch (c) {
	case '-':
		dataset[pointer]--;
		dataset[pointer] %= 256;
		break;
	case '+':
		dataset[pointer]++;
		dataset[pointer] %= 256;
		break;
	case '<':
		if (pointer == 0)
			pointer = m - 1;
		else pointer--;
		break;
	case '>':
		if (pointer == m - 1)
			pointer = 0;
		else pointer++;
		break;
	case '[':
		if (dataset[pointer] == 0)
			jump(k);
		//짝을 이루는 곳으로 점프
		break;
	case ']':
		if (dataset[pointer] != 0)
			jump(k);
		break;
	case '.':
		if (dataset[pointer] != 0);
		//printf("%d", dataset[pointer]);
		break;

	case ',':
		if (scancount < s)
			dataset[pointer] = str[scancount];
		else
			dataset[pointer] = 255;
		scancount++;
		break;
	}
}



void jump(int location) {
	int jump_pointer = location;


	int i = jump_pointer;
	bool flag = false;
	while (!flag) {
		if (brainfuck[i] == '[') {
			if (dataset[pointer] != 0) {
				flag = true;
				break;
			}


			vector<char> myvector;
			myvector.push_back('[');
			while (!myvector.empty()) {
				i++;
				if (brainfuck[i] == '[')
					myvector.push_back('[');

				else if (brainfuck[i] == ']')
					myvector.pop_back();
			}
	
			count_times++;
			//pointer = i;
			k = i;
		}



		else if (brainfuck[i] == ']') {
			if (dataset[pointer] == 0) {
				flag = true;
				break;
			}
			vector<char> myvector;
			myvector.push_back(']');
			while (!myvector.empty()) {
				i--;
				if (brainfuck[i] == ']')
					myvector.push_back(']');

				else if (brainfuck[i] == '[')
					myvector.pop_back();
			}
		
			count_times++;
			//pointer = i;
			k = i;
		}


		if (count_times > 50000000 && brainfuck[i] == '[')
			flag = true;
	}


}