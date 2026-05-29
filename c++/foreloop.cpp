#include <iostream>
#include <string>


std::string name_string[10] = {
    "one", "two", "three", "four", "five",
    "six", "seven", "eight", "nine"
};

int main(){
    int x, y;
    std::cin>>x>>y;


    for(int i=x; i<=y ; i++){
        if(i >= 1 && i <= 9){
            std::cout<<name_string[i-1]<<'\n';
        }
        else if(i % 2 == 0){
            std::cout<<"even\n";
        }
        else{
            std::cout<<"odd\n";
        }
    }
    

}
