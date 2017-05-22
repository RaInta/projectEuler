/*
 * C program to check whether a given number is prime or not
 * and output the given number with suitable message.
 */
#include <stdio.h>
#include <stdlib.h>
 
void main()
{
    int num, j, flag;
 
    printf("Enter a number \n");
    scanf("%d", &num);
 
    if (num <= 1)
    {
        printf("False", num);
        exit(1);
    }
    flag = 0;
    for (j = 2; j <= num / 2; j++)
    {
        if ((num % j) == 0)
        {
            flag = 1;
            break;
        }
    }
    if (flag == 0)
        printf("True", num);
     else
        printf("False", num);
}
