#include<iostream>
#include<bitset>
#include<string>
using namespace std;

int main(int argc, char **argv){
    int x=8;
    bitset<8> b(x);
    cout<<b<<endl;
    system("pause");
    return 0;
}