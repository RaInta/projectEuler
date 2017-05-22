#include <math.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[] )
{
    printf("Program name %s\n", argv[0]);
    printf("Argument: %s \n", argv[1]);
    float x; 
    x = atof(argv[1]);
    printf("The float version: %f \n", x);
    printf("ROUnded: %4.2f \n", ceil(x) );   
    return 0;
}

