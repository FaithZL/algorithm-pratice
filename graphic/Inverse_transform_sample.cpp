/*
* @Author: ZhuL
* @Date:   2018-10-01 12:44:01
* @Last Modified by:   ZhuL
* @Last Modified time: 2018-10-01 21:24:20
*/

#include <iostream>
#include <iomanip>
#include <string>
#include <map>
#include <random>
#include <cmath>
#include <cstdlib> 
#include <cstring> 
#include <algorithm> 
#include <vector>

using namespace std;

double normalPdf(double x) {
	double mu = 0;
	double sigma = 1;
	return 1 / (sqrtf(2 * M_PI) * sigma) * exp(-(x - mu) * (x - mu) / (2 * sigma * sigma));
}

class Sampler
{
public:
	Sampler() {}
	~Sampler() {
		clearCdf();
	}

	Sampler(std::function<double(double)> pdf , int count , double min , double max) {
		createCdf(pdf , count , min , max);
	}

	void createCdf(std::function<double(double)> pdf , int count , double min , double max) {
		this->_min = min;
		this->_max = max;
		clearCdf();
		_cdf_a = new double[count + 1];
		_cdf_a[0] = 0;
		double dx = (max - min) / count;
		for (int i = 1; i < count; ++i) {
			double x = min + i * dx;
			double dy = dx * pdf(x);
			_cdf_a[i] = _cdf_a[i - 1] + dy;
		}

		_cdf_a[count] = 1;
		_count = count;
	}

	double random() {
		double r = drand48();
		double ret;
		double * ptr = std::lower_bound(_cdf_a , _cdf_a + _count + 1 , r);
		int offset = ptr - _cdf_a;
		return _min + (offset * 1.0 / _count) * (_max - _min);
	}

	void setCdf(std::function<double(double)> cdf) {
		this->cdf = cdf;
	}

	void outputCdf() {
		for (int i = 0; i < _count + 1; ++i) {
			cout << _cdf_a[i] << endl;
		}
	}

protected:

	void clearCdf() {
		if (_cdf_a != nullptr) {
			delete [] _cdf_a;
			_cdf_a = nullptr;
		}
	}

	double * _cdf_a = nullptr;

	std::function<double(double)> cdf;

	int _count;

	double _min;

	double _max;
	
};


int main()
{
	// srand((unsigned)time(0));
	auto sampler = Sampler(normalPdf , 10000 , -100 , 100);
 
    std::map<int, int> hist{};
    for(int n=0; n<10000; ++n) {
        ++hist[sampler.random()];
    }
    for(auto p : hist) {
        std::cout << std::setw(2)
                  << p.first << ' ' << std::string(p.second/200, '*') << '\n';
    }
}
// output like
// -3 
// -2 *
// -1 ******
//  0 *********************************
//  1 ******
//  2 *
//  3 