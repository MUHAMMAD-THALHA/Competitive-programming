//  calculate and print the difference between the sum of odd and even elements in an array:

#include <iostream>
#include <vector>

using namespace std;

int main() {
    int N;
    cin >> N; 
    vector<int> arr(N);  
    int evenSum = 0, oddSum = 0;

    for(int i = 0; i < N; i++) {
        cin >> arr[i]; 
        if(arr[i] % 2 == 0) {
            evenSum += arr[i]; 
        } else {
            oddSum += arr[i]; 
        }
    }

    int difference = oddSum - evenSum;  
    cout << difference << endl; 
    return 0;
}
