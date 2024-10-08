// GREATEST OF THREE NUMBERS 

#include <iostream>
#include <algorithm> 
using namespace std;

int main() {

    double num1, num2, num3;

    cin >> num1 >> num2 >> num3;

    double greatest = max({num1, num2, num3});

    cout << greatest << endl;

    return 0;
}
