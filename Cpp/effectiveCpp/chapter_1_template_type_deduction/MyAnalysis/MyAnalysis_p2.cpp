//Custom
#include <iostream>

/// REVIEW CODE:
/// 
/// template<typename T>
/// void f(ParamType param);
///
/// f(expr); // deduce T and ParamType from expr
///

template<typename T>
void f(T param){ // param is now passed by value 
	std::cout << "param: " << param << std::endl;
}

int main (int argn, char **argc) {


	int x = 27; // x is an int
	const int cx = x; // cx is a const int
	const int& rx = x; // rx is a reference to x as a const int

	// in all 3 calls argument will be passed as int and copy of argument will be created
	f(x);   // int
	f(cx);  // ignore const
	f(rx);  // ignore reference and const

	return 0;
  
}


