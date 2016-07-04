#include <cmath>
#include "nr.h"
#include "gammln.cpp"
using namespace std;

DP NR::factrl(const int n)
{
	static int ntop=4;
	static DP a[33]={1.0,1.0,2.0,6.0,24.0};
	int j;

	if (n < 0) nrerror("Negative factorial in routine factrl");
	if (n > 32) return exp(gammln(n+1.0));
	while (ntop<n) {
		j=ntop++;
		a[ntop]=a[j]*ntop;
	}
	return a[n];
}

int main()
{
	int number,out;
	number = 6; 
	out = NR::factrl(number);
	cout<<out<<endl;	

	return 0;
}