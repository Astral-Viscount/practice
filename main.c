#include <stdio.h>
#include <stdlib.h>

//Functions
int guessing_game(void);

int main()
{

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