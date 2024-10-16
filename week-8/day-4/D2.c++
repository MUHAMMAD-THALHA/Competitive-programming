// Swap Question in c++ : 
  
#include <iostream>
#include <cstdio>
#include <vector>
Using namespace std;

Int main() {
 int a,b;
 
 cin >> a >> b; 
 
 a = a + b;
 b = a - b;
 a = a - b;
 
 cout << "After swapping" << a << " " << b << endl;
 
 return 0;

}
 