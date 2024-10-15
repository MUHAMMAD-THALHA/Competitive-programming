// WRITE A PROGRAM TO FIND AND PRINT INDICES OF A GIVEN ELEMENT IN AN ARRAY.

#include <iostream>
#include <vector>

using namespace std;

int main() {
    int N;
    cin >> N;

    vector<int> arr(N);
    for (int i = 0; i < N; i++) {
        cin >> arr[i];
    }

    int element;
    cin >> element;

    bool found = false;
    for (int i = 0; i < N; i++) {
        if (arr[i] == element) {
            cout << i << " ";
            found = true;
        }
    }

    if (!found) {
        cout << "-1";
    }

    cout << endl;

    return 0;
}