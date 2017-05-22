#include <math.h> 
#include <stdio.h>
#include <stdlib.h>

int collatz(int m);

int main(int argc, const char *argv[])
{
    
    int n,r, chainCount, maxChain, nMax, nBig;
    nMax = atoi(argv[1]);
    maxChain = 0;
    for (n = 1; n < nMax; n++) {
        chainCount=2;
        r = collatz(n);
        while ( r > 1)
        {
            /*printf("%d\n",r);*/
            r=collatz(r);
            chainCount++;
    }
        if (chainCount > maxChain) {
            maxChain = chainCount;
            nBig = n;
        }
    }
    printf("The largest chain is %d, from %d \n", maxChain, nBig);
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
