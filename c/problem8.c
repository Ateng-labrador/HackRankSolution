#include <stdio.h>

// Bitwise Operators
// Bitwise AND operator &
// Bitwise OR operator |
// Bitwise XOR (exclusive OR) operator ^

int find_max_AND(int a, int b){
    int maxAND = 0;
    for(int i = 1; i<= a; i++){
        for(int j = i+1; j<=a; j++){
            int AND = i & j;
            if(AND < b && maxAND < AND)  maxAND = AND;
        }
    }
    return maxAND;
}

int find_max_OR(int a, int b){
    int maxOR = 0;
    for(int i = 1; i<= a; i++){
        for(int j = i+1; j<=a; j++){
            int OR = i | j;
            if(OR < b && maxOR < OR)  maxOR = OR;
        }
    }
    return maxOR;
}

int find_max_XOR(int a, int b){
    int maxXOR = 0;
    for(int i = 1; i<= a; i++){
        for(int j = i + 1; j<=a; j++){
            int XOR = i ^ j;
            if(XOR < b && maxXOR < XOR)  maxXOR = XOR;
        }
    }
    return maxXOR;
}


int main(){
    int n, m;
    scanf("%d %d", &n, &m);
    printf("%d\n", find_max_AND(n, m));
    printf("%d\n", find_max_OR(n, m));
    printf("%d", find_max_XOR(n, m));
    return 0;
}
