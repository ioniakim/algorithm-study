#include <iostream>
#include <vector>
#include <string>

#define RANGE 255
using namespace std;

/**
 * C: Container Type of CHAR
 */
template<typename C>
void countingSort(C& arr)
{
    C output(arr.size(), 0);
    char count[RANGE] = {0,};

    for(auto& c : arr){
        ++count[c];
    }

    for(int i = 1 ; i < RANGE ; ++i){
        count[i] += count[i-1];
    }

    for(auto& c : arr){
        output[--count[c]] = c;
    }

    arr.assign(output.begin(), output.end());
}

int main()
{
    std::vector<char> arr = {'c', 'b', 'c', 0, 'a', 's', 'l'};
    countingSort(arr);
    for(auto& c : arr){
        cout << c << ',';
    }
    cout << endl;

    string str = "wlfjlwflwe";
    countingSort(str);
    cout << str << endl;
    return 0;
}