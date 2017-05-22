#include <math.h> 
#include <stdio.h>
#include <stdlib.h>

int collatz(int m);

int main(int argc, const char *argv[])
{
    
    if (argc==1) {
        printf("Warning! No argument given.\n");
        return 1;
    }
    int n,r;
    n = atoi(argv[1]);
    r = collatz(n);
    while ( r > 1)
    {
        printf("%d\n",r);
        r=collatz(r);
    }
    return 0;
}

int collatz(int m)
{
    if (( m % 2) == 0 ) {
        return m/2;
    }
    else
    {
        return 3*m+1;
    }
}
