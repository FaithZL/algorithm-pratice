/*
* @Author: ZhuL
* @Date:   2018-07-04 23:41:38
* @Last Modified by:   ZhuL
* @Last Modified time: 2018-07-05 00:27:12
*/


#include "a-star.hpp"
#define M 16

using namespace std;

static int arr[M][M] = {
	{0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0},
	{0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0},
	{0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0},
	{0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0},
	{0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0},
	{0 , 0 , 0 , 0 , 0 , 0 , 0 , 1 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0},
	{0 , 0 , 0 , 0 , 0 , 0 , 0 , 1 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0},
	{0 , 0 , 0 , 0 , 0 , 0 , 0 , 1 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0},
	{0 , 0 , 0 , 0 , 0 , 0 , 0 , 1 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0},
	{0 , 0 , 0 , 0 , 0 , 2 , 0 , 1 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0},
	{0 , 0 , 0 , 0 , 0 , 0 , 0 , 1 , 0 , 0 , 2 , 0 , 0 , 0 , 0 , 0},
	{0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0},
	{0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0},
	{0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0},
	{0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0},
	{0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0},
};

static Node * nodeArr[M][M];

void genNodeArr(Node * na[M][M] , int ia[M][M]) {
	for (int i = 0; i < M; ++i) {
		for (int j = 0; j < M; ++j) {
			na[i][j] = Node::create(i , j , ia[i][j]);
		}
	}
}

void release(Node * na[M][M]) {
	for (int i = 0; i < M; ++i) {
		for (int j = 0; j < M; ++j) {
			auto p = na[i][j];
			if (p != nullptr)
			{
				delete p;
				na[i][j] = nullptr;
			}
		}
	}	
}

void output(int a[][M]) {
	for (int i = 0; i < M; ++i) {
		for (int j = 0; j < M; ++j) {
			cout << a[i][j] << " ";
		}
		cout << endl;
	}
}

int main(int argc, char const *argv[]) {
	
	output(arr);

	genNodeArr(nodeArr , arr);

	return 0;
}