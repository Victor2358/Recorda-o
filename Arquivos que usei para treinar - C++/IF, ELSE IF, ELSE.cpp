#include <iostream>
using namespace std;

int main(){
    int a;

    if (a == 10) // Here, the == means "equal"
    {
        std::cout << "Something will appear here \n";
    }
    else if (a == 20)
    {
        std::cout << "Another thing will happen here \n";
    }
    else
    {
        std::cout << "The last chance. Something will happen here, still nothing happened before \n";
    }
    return 0;
}