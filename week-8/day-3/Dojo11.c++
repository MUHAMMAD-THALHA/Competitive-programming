// Print the indices of a given element in an array. 


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

    int sum = arr[0] + arr[1];
    cout << sum << endl;

    return 0;
}
