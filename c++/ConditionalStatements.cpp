#include <iostream>
#include <string>

std::string name_number[10] = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"};

int main(){
    std::string n_temp;
    std::getline(std::cin, n_temp);

    if(n_temp == "1"){
        std::cout<<name_number[0]<<std::endl;
    }
    else if(n_temp == "2"){
        std::cout<<name_number[1]<<std::endl;
    }
    else if(n_temp == "3"){
        std::cout<<name_number[2]<<std::endl;
    }
    else if(n_temp == "4"){
        std::cout<<name_number[3]<<std::endl;
    }
    else if(n_temp == "5"){
        std::cout<<name_number[4]<<std::endl;
    }
    else if(n_temp == "6"){
        std::cout<<name_number[5]<<std::endl;
    }
    else if(n_temp == "7"){
        std::cout<<name_number[6]<<std::endl;
    }
    else if(n_temp == "8"){
        std::cout<<name_number[7]<<std::endl;
    }
    else if(n_temp == "9"){
        std::cout<<name_number[8]<<std::endl;
    }
    else{
        std::cout<<"Greater than 9"<<std::endl;
    }


    return 0;
}
