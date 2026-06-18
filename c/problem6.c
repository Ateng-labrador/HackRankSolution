#include <stdio.h>


void speaking_number(int n, int m){
    const char *number[] = {
        "one", "two", "three", 
        "four", "five", "six",
        "seven","eight", "nine"};
    for(int i = n; i <=m; i++){
        if(i >= 1 && i<= 9){
            printf("%s\n", number[i-1]);
        }
        else if (i % 2 == 0){
            printf("even\n");
        }
        else{
            printf("odd\n");
        }
    }
}


int main(){
    int n, m;
    scanf("%d", &n);
    scanf("%d", &m);
    speaking_number(n, m);
}
