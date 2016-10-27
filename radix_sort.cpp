// C++ implementation of Radix Sort
#include <iostream>

using namespace std;

/**
 * Get maximum value in arr[]
 * @param  arr array of values out of which the max value is to get
 * @param  n   the size of arr
 * @return     maximum value
 */
int getMax(int arr[], int n)
{
    int max = arr[0];
    for (int i = 1; i < n; ++i){
        if (arr[i] > max){
            max = arr[i];
        }
    }
    return max;
}

/**
 * A function to do counting sort of arr[] according to the digit represented
 * by exp.
 * @param arr [description]
 * @param n   [description]
 * @param exp [description]
 */
void countSort(int arr[], int n, int exp)
{
    int output[n];
    int i, count[10] = {0};

    for(i = 0; i < n; ++i){
        count[(arr[i]/exp)%10]++;
    }

    for(i = 1; i < 10; ++i){
        count[i] += count[i - 1];
    }
}