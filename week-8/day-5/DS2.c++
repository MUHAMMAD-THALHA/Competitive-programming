//a program to calculate the ticket price for a movie theater. The theater offers different pricing based on the age of the moviegoer and the time of the movie.

#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    int age, hour;
    cin >> age >> hour;

    int ticket_price = 10; 

    if (age <= 12) {
        ticket_price = 5;
    } else if (age >= 60) {
        ticket_price = 6;
    }

    if (hour < 12) {
        ticket_price -= 2;
    } else if (hour >= 18) {
        ticket_price += 1;
    }

    cout << "Ticket price: $" << ticket_price << endl;

    return 0;
}