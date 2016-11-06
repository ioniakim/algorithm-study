// testing range-based for loop on set

#include <set>
#include <iostream>

using namespace std;

int main(int argc, const char *argv[])
{
    set<int> s = {1, 2, 3};

    for (const auto &i : s){
        cout << i << ' ' ;
    }

    cout << endl;
    return 0;
}