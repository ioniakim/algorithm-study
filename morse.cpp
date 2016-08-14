#include <iostream>
#include <string>

using namespace std;

void morse(int n, int m, string s){
    if (0 == n && 0 == m){
        cout << s << endl;
    }

    if (n > 0){
        morse(n - 1, m, s + '-');
    }

    if (m > 0){
        morse(n, m - 1, s + 'o');
    }
}

int k;

void morse2(int n, int m, string s){
    if (0 > k){
        return;
    }

    if (0 == n && 0 == m){
        if (0 == k){
            cout << s << endl;
        }
        k--;
        return;
    }

    if (0 < n) {
        morse2(n-1, m, s + '-');
    }
    if (0 < m){
        morse2(n, m-1, s + 'o');
    }
}

int main(){
    string s;
    k = 100000;
    morse2(100, 100, s);
    // morse(3, 3, s);
}