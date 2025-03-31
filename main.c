//Header Files
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <stdbool.h>

//Functions
int guessing_game(void);
int computer_guessing_game(void);
int bad_calculator(void);
void is_even(void);

//Main Function
int main(void)
{
    printf("Hello, World!");
    return 0;
}

//Guessing game
int guessing_game(void)
{
    // Generate a random number using the rand() function
    int upp = 100;
    int low = 1;
    int num = rand() % (upp - low + 1) + low;

    int guess = 0;

    printf("   Welcome to the number guessing game!\n");
    printf("<<------------------------------------->>\n\n");

    while (1 == 1)
    {
        int user;
        printf("Guess the number: ");
        scanf("%i", &user);

        if (user > num)
        {
            printf("The number is smaller!\nTry again!");
            guess++;
        }
        else if (user < num)
        {
            printf("The number is bigger!\nTry again!");
            guess++; 
        }
        else
        {
            printf("\nCorrect!!! ");
            printf("It took you %i guesses to get the correct number!\n", guess);
            break;
        }       
    }
}

//Guessing Game (Computer)
int computer_guessing_game(void)
{
    int high = 100;
    int low = 1;
    int guess;

    char feedback[10];

    while (1)
    {
        guess = rand() % (high - low + 1) + low;

        printf("Is the number %i too high(H) or too low(L) or correct(C): ", guess);
        scanf("%s", &feedback);

        feedback[0] = tolower(feedback[0]);

        if (strcmp(feedback, "h") == 0)
        {
            high = guess - 1;
        }
        else if (strcmp(feedback, "l") == 0)
        {
            low = guess + 1;
        }
        else if (strcmp(feedback, "c") == 0)
        {
            printf("Yay! The computer guessed your number, %i, correctly!!!\n", guess);
            break;
        }
    }
}

//Factorial!
int factorial(void)
{
    int num;
    printf("Number: ");
    scanf("%i", &num);

    int fact = 1;

    for(int i = 1; i < num + 1; i++)
    {
        fact *= i;
    }

    printf("%i! = %i", num, fact);
}

//Bad Calculator
int bad_calculator(void)
{
    int num;
    printf("Enter a Number: ");
    scanf("%i", &num);

    int low = 1;
    int x = rand() % (num - low + 1) + low;

    int y = num - x;

    printf("%i + %i = %i", x, y, num);
}

// Function to check if a number is even using recursion
bool even(int n)
{
    if (n < 0) // Handle negative numbers
        return even(-n);

    if (n == 0)
        return true;
    if (n == 1)
        return false;

    return even(n - 2);
}

// Function to get user input and determine even/odd
void is_even(void)
{
    int num;
    printf("Number: ");
    scanf("%i", &num);

    if (even(num))
        printf("%i is an even number!\n", num);
    else
        printf("%i is an odd number!\n", num);
}
