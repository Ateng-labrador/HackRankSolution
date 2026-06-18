#include <stdio.h>

int penjumlahan(int n){
    int res = 0;
    while (n != 0){
        res = res + n % 10;
        n /= 10;
    }
    return res;
}

int main(){
    int n;
    scanf("%d", &n);
    printf("%d", penjumlahan(n));
}
