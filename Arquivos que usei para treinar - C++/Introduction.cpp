#include <iostream>
using namespace std;

int main()
{

    int score; // Declare a variable
    score = 0; // Initialize a variable

    int age;
    cout << "How old are you? "; // << is the output operator
    cin >> age; // >> is the input operator
    cout << "You're " << age << " years old\n";

    // cin = character input
    // cout = character output

    string name;
    cout << "What's your name? ";
    cin >> name;
    cout << "Your name is " << name << "? It's a cool name!";

    return 0;
}