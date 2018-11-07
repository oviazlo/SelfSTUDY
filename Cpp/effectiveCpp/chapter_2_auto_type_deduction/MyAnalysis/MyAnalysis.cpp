//Custom
#include <iostream>


// template <typename T>
// void f1(T param){} 	// template with parameter
			// declaration equivalent to
			// x's declaration

template <typename T>
void f2(std::initializer_list<T> initList){}

int main (int argn, char **argc) {

	/// TOPIC 1: deduction of type with auto during initialization
	
	auto x1 = 27; 		// type is int, value is 27

	auto x2(27); 		// ditto

	auto x3 = { 27 }; 	// type is std::initializer_list<int>,
				// value is { 27 }

	auto x4{ 27 }; 		// ditto

	/// "auto" can handle {} --> deduce it as std::initializer_list<T> in first step. Second step is deduction of "T". 
	 
	// auto x5 = { 1, 2, 3.0};	// error! can't deduce T for
	//				// std::initializer_list<T>


	auto x = { 11, 23, 9 }; // x's type is
				// std::initializer_list<int>
	
	/// TOPIC 2: Difference between "auto" deduction during initialization
	/// and template type deduction
	
	/// template type deduction cannot handle braced initializer ({})
	/// void f1(T param):
	
	// f1({ 11, 23, 9 }); 	// error! can't deduce type for T
	
	/// however this function will work: 
	/// void f2(std::initializer_list<T> initList){} 
	f2({ 11, 23, 9 });
	
	/// TOPIC 3: auto deduction for function's return 
	/// "auto" for functions is the same as template deduction
	//
	// Example:
	// auto createInitList()
	// {
	//         return { 1, 2, 3 };
	// }
	// ERROR: can't deduce type
	// for { 1, 2, 3 }

	/// "auto" in lambda functions use template deduction as well
	//
	// Example:
	// std::vector<int> v;
	// ...
	// auto resetV = [&v](const auto& newValue) { v = newValue; };
	// ...
	// resetV({ 1, 2, 3 }); // ERROR! can't deduce type

	return 0;
}


