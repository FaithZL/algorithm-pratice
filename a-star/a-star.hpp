
#include <cmath>
#include <iostream>
#include <vector>

class Node
{
public:
	Node() {

	}

	~Node() {

	}

	static Node * create(int i , int j , int val) {
		Node * ret = new Node();
		ret->_i = i;
		ret->_j = j;
		ret->_val = val;
		return ret;
	}

	double getG() {
		return _G;
	}

	double getH() {
		return _H;
	}

	double getF() {
		return getH() + getG();
	}

	double calAndSetH(int i , int j) {
		int di = fabs(i - _i);
		int dj = fabs(j - _j);	
		_H = (di + dj) * 10;	
		return _H;
	}

	Node * getParent() {
		return _parent;
	}

	void setParent(Node * parent) {
		_parent = parent;
	}

	double calAndSetG(int i , int j) {
		int di = fabs(_i - i);
		int dj = fabs(_j - j);

		if (di > dj) {
			int i1 = di - dj;
			_G = i1 * 10 + 14 * dj;
		} else if (di < dj) {
			int j1 = dj - di;
			_G = j1 * 10 + 14 * di;
		} else {
			_G = 14 * di;
		}
		return _G;		
	}
	
protected:
	int _i;
	int _j;
	int _G = -1;
	int _H = -1;
	int _val;
	Node * _parent = nullptr;
};