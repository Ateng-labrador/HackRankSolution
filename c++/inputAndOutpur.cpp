#include <iostream>

int x;
int y;
int z;

int penjumlahan(int a, int b, int c){
    return a + b + c;
}

int main(){
    std::cin>>x>>y>>z;
    std::cout<<penjumlahan(x, y, z)<<std::endl;
}
