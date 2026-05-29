#include <iostream>
#include <cstdio>


int d;
long f;
char c;
float e;
double k;

int main(){
    scanf("%d %ld %c %f %lf", &d, &f, &c, &e, &k);
    printf("%d \n%ld \n%c \n%f \n%lf", d, f, c, e, k);
    

    return 0;
}
    // std::cout<<d<<std::endl;
    // std::cout<<f<<std::endl;
    // std::cout<<c<<std::endl;
    // std::cout<<e<<std::endl;
    // std::cout<<k<<std::endl;

    /*

data types in c++

-> int("%d"): 32 bit integer
-> long("%ld"): 64 bit integer
-> char("%c"): character type
-> float("%f"): 32 bit real value
-> double("%lf"): 64 bit real value

scanf("`format_specifier`", &val)
int, long, char, float, and double, respectively

*/