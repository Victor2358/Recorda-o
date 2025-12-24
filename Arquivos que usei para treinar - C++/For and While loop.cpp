#include <iostream>
using namespace std;

int main()
{
    // For loop
    for(int i = 100; i <= 105; i++)
    {
        std::cout << i;
        std::cout << "\n";
    }

    // While loop    
    int contador_three = 0;
    while (contador_three <= 20)
    {
        std::cout << contador_three;
        std::cout << "\n";
        contador_three++;
    }

    std::cout << "\n";

    // Do-While loop
    int contador_four = 20;
    do
    {   
        std:: cout << contador_four;
        std:: cout << "\n";
        contador_four++;
    } while (contador_four <= 40); //Here the while have parenthesis
    return 0;
}