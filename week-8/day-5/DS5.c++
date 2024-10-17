// Calculate average and sum of the elements in an array.
#include <iostream>
#include <vector>
#include <iomanip> 

using namespace std;

int main() {
    int N;
    cin >> N; 
    
    vector<int> arr(N); 
    int sum = 0;

    for(int i = 0; i < N; i++) {
        cin >> arr[i];  
        sum += arr[i]; 
    }

    double average = static_cast<double>(sum) / N;  


    cout << sum << endl;
    cout << fixed << setprecision(2) << average << endl;

    return 0;
}
