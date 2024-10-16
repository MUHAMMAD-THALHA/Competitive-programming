// Calculate the perimeter and area 

#include <iostream>
#include <cmath> 
using namespace std;

int main() {
    double radius;
    cin >> radius;
    
    double perimeter = 2 * M_PI * radius;
    double area = M_PI * radius * radius;

    cout << "Perimeter: " << fixed << perimeter << endl;
    cout << "Area: " << fixed << area << endl;

    return 0;
}