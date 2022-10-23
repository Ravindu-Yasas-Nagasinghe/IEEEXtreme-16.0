// include the standard C++ headers
#include <iostream>         // for standard I/O
#include <fstream>          // for file I/O: https://cplusplus.com/reference/fstream/fstream/
#include <bits/stdc++.h>    // for standard C++ headers
using namespace std;

int main(){
    string input;
    cin >> input;

    bool alloff = false;
    int len = input.size();
    
    while(!alloff){
        for(int i =0; i < len; i++){
            
            // switch condition check
            if(i < len-2){

                string ip2onward = input.substr(i+2);
                int sublen = ip2onward.size();
                bitset<50> sub(ip2onward);
                int ones = (int)__builtin_popcount(sub.to_ulong());

                if(input[i+1] ==  '1' && ones == 0){
                    if(input[i] == '1'){
                        input[i] == '0';
                    }else{
                        input[i] == '1';
                    }
                }
            }else if()
            
            
        }
    }
}