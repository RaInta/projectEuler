#include <math.h> 
#include <stdio.h>
#include <stdlib.h>

int main(int argc, const char *argv[])
{
    
    int n, i;
    if (argc==1) {
        printf("Warning! No argument given.\n");
        return 1;
    }
    int factorCount = 0;
    n = atoi(argv[1]);
    int l = ceil(sqrt(n));
            for ( i = 2; i < l; i++ ) 
            {
                if ( (n % i) == 0 ) 
                {
                    printf("%d\n",i);
                    factorCount++;
                }
            }
            factorCount++;
            factorCount = 2*factorCount;
            if ( (int)n == pow(l, 2 ) ) 
            {
                factorCount++;
            }
    printf ( "%d\n", factorCount ); 
    return 0;
}

