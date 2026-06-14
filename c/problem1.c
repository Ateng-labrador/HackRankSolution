#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main(){
    // deklarasi tipe data
    char s[100];
    // membaca input 
    scanf("%[^\n]%*c", &s);
    printf("Hello, World!");
    printf("\n");
    printf("Welcome to C programming.");
    return 0;
}

