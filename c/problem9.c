#include <stdio.h>
#include <math.h>
#include <string.h>


void print(int a){
    for(int i = a; i>= 1; i--){
        for(int j = a; j > i; j--)
            printf("%d", j);
        for(int j = 1; j <= 2 * i - 1; j++)
            printf("%d", j);
        for(int j = i + 1; j <= a; j++)
            printf("%d", j);
        printf("\n");
    }

    for(int i = 1; i < a; i++){
        for(int j = a;j > i; j--)
            printf("%d", j);
        for(int j = 1;j <= 2 * i - 1; j++)
            printf("%d", i + 1);
        for(int j = i + 1; j <= a; j++)
            printf("%d", j);
        printf("\n");
    }
}


int main(){
    int n;
    scanf("%d", &n);
    print(n);
}
