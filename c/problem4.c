#include <stdio.h>
#include <math.h>


void update(int *a, int *b){
    printf("%d\n", *a + *b);
    printf("%d", abs(*a - *b));
}

int main(){
    int a, b;
    scanf("%d", &a);
    scanf("%d", &b);
    update(&a, &b);
    return 0;
}