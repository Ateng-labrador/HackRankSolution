#include <iostream>


void absoulute(int *a, int *b){
    int a_sum = *a + *b;
    int b_sum = abs(*b - *a);
    std::cout<<a_sum<<'\n'<<b_sum<<std::endl;
    
}

int main(){
    int a, b;
    int *aPtr = nullptr;
    int *bPtr = nullptr;
    std::cin>>a>>b;
    aPtr = &a;
    bPtr = &b;
    absoulute(aPtr, bPtr);

}
