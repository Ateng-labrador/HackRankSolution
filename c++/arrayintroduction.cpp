#include <iostream>
#include <algorithm>
#include <cstdio>




int main(){
    int N;
    std::cin>>N;
    int arr[N];

    int n = sizeof(arr) / sizeof(arr[0]);

    for(int i = 0; i<N; i++){
        std::cin>> arr[i];
    }
    
    std::reverse(arr, arr + n);
    for (int i: arr){
        std::cout<<i<<" ";
    }
    
    return 0;
}
