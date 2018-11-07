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
void f(T&& param){ // param is a UNIVERSAL reference 
	std::cout << "param: " << param << std::endl;
}

int main (int argn, char **argc) {


	int x = 27; // x is an int
	const int cx = x; // cx is a const int
	const int& rx = x; // rx is a reference to x as a const int

	// argument is lvalue
	f(x);
	f(cx);
	f(rx);
	// argument is rvalue
	// no complains from compilor since param is a universal reference!!!
	// if it would be regular reference (i.e. only one "&") call below will invoke complains from compiler!!!
	f(27);	

	return 0;
  
}


