// Check if the character is vowel either it is uppercase or lowercase and check whether the first and last letter is vowel or not .

#include <iostream>
#include <string>
using namespace std;

bool isVowel(char c) {
    c = tolower(c);  
    return (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u');
}

int main() {
    string word;
    cin >> word;  

    char firstLetter = word[0];
    char lastLetter = word[word.length() - 1];

    if (isVowel(firstLetter) && isVowel(lastLetter)) {
        cout << "Vowel" << endl;
    } else {
        cout << "Not Vowel" << endl;
    }

    return 0;
}