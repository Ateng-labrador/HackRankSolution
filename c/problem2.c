#include <stdio.h>

int main(){
    char s[100];
    char f[100];
    char z[100];

    scanf("%[^\n]%*c", s);
    scanf("%[^\n]%*c", f);
    scanf("%[^\n]%*c", z);
    printf(s);
    printf("\n");
    printf(f);
    printf("\n");
    printf(z);
    return 0;
}