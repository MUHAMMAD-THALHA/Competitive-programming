//  COMPLETED QUADRATIC EQUATION AND ITS COEFFICIENTS IN C++


#include <iostream>
using namespace std;

int main() {
    double a,b,c ;

    cout << "" ;

    cin >> a >> b >> c ;

    if (a==0) {
        cout << "Invalid input" ;

        return 0;
    }

    double discriminant  = b * b - 4 * a * c;

    if (discriminant > 0) {
        
        cout << "Real and Distict" << endl;

    } else if (discriminant == 0 ) {

        cout << "Real and Equal" << endl;

    } else {

        cout << "Complex" << endl;

    }

    return 0;

}