//  Check if the character is a vowel (either uppercase or lowercase)

#include <iostream>
#include <string>
using namespace std;

int main() {
    string input;
    getline(cin, input);  

    for (char c : input) {
        
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' || 
            c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U') {
            cout << c << " ";         }
    }

    return 0;
}