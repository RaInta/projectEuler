#include <math.h> 
#include <stdio.h>
#include <stdlib.h>

/* Note that, although this is whoppingly fast, this still overflows for N~>100000*/

long countAllFactors( unsigned long long t );
unsigned long long triangleNum(unsigned long long m);


int main(int argc, const char *argv[])
{
    if (argc==1) {
        printf("Warning! No argument given.\n");
        return 1;
    }
    unsigned long long n, tNum; 
    long triangleDiv;
    /* n = atol(argv[1]);*/
    n = strtol(argv[1], NULL, 0);
    tNum = triangleNum(n);
    triangleDiv = countAllFactors( tNum );
    /*printf ( "%d", triangleDiv );*/
    printf ( "Number: %d \n", n ); 
    printf ( "Triangle number: %d \n", tNum ); 
    printf ( "Number of divisors: %d \n", triangleDiv );
    return 0;
}


unsigned long long triangleNum( unsigned long long t )
{
    unsigned long long i;
    unsigned long long summa = 0;
    for (i = 0; i < t+1; i++) {
        summa += i;
    }
    return summa;
}

long countAllFactors( unsigned long long m )
{
    
    unsigned long long i, l;
    long factorCount = 0;
    l = ceil(sqrt( m ));
            for ( i = 2; i < l; i++ ) 
            {
                if ( (m % i) == 0 ) 
                {
                    factorCount++;
                }
            }
            factorCount++;
            factorCount = 2*factorCount;
            if ( m == pow(l, 2 ) ) 
            {
                factorCount++;
            }
    return factorCount;
}
