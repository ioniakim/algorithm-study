#include <iostream>
#include <algorithm>

#include <cstring> // to use memset function

using namespace std;

int n;
int cache[101], S[100];

int lis(int start){
    int& ret = cache[start+1];
    if(ret != -1) return ret;

    ret = 1;
    for (int next = start+1 ; next < n; ++next){
        if(start == -1 || S[start] < S[next]){
            ret = max(ret, lis(next) + 1);
        }
    }
    return ret;
}

int main(){
    n = 5;
    S[0] = 5;
    S[1] = 4;
    S[2] = 3;
    S[3] = 2;
    S[4] = 1;

    memset(cache, -1, sizeof(cache));
    cout<< lis(-1) << endl;
}