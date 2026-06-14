#include <stdio.h>

int max_of_four(int a, int b, int c, int d){
    int number[] = {a, b, c, d};
    int size = sizeof(number) / sizeof(number[0]);
    int max = number[0];

    for(int i = 1; i < size; i++){
        if(number[i] > max){
            max = number[i];
        }
    }
    return max;
}

int main(){
    int a, b, c, d;
    scanf("%d", &a);
    scanf("%d", &b);
    scanf("%d", &c);
    scanf("%d", &d);
    printf("%d", max_of_four(a, b, c, d));
}