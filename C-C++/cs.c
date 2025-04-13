#include <stdio.h>

int main(void)
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
