// VOWEL OR NOT VOWEL IN C++

#include <iostream>
using namespace std;

int main() {

    char ch;

    cout << "";

    cin >> ch ;

    ch = tolower(ch);

    if (ch == 'a' || ch == 'e' || ch == 'i' ch == 'o' || ch == 'u') {
        cout << ch << "Vowel" << endl ;

    } else {

        cout << ch << "Not Vowel" << endl ;
    }

    return 0;

}