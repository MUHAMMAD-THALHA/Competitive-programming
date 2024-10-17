// Write a program that takes an integer.

#include <iostream>
#include <string>
using namespace std;

int main(){
    long long num;
    cin >> num;

    if (num%2 == 0) {
        cout << "Even" << endl;
    } else {
        cout << "Odd" << endl;
    }

    return 0;
}