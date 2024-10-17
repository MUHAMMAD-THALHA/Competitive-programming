// Write a program to read the temperature in centigrade and display a suitable message according to the temperature state below.

#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
using namespace std;

int main() {
    int Temp;
    cin >> Temp;

    if (Temp < 0) {
        cout << "Freezing Weather" << endl;
    } else if (Temp >= 0 && Temp <= 10) {
        cout << "Very cold weather" << endl;
    } else if (Temp >= 11 && Temp <= 20) {
        cout << "Cold weather" << endl;
    } else if (Temp >= 21 && Temp <= 30) {
        cout << "Normal in temp" << endl;
    } else if (Temp >= 31 && Temp <= 40) {
        cout << "It's hot" << endl;
    } else if (Temp > 40) {
        cout << "It's very hot" << endl;
    } else {
        cout << "Invalid input" << endl;
    }

    return 0;
}
