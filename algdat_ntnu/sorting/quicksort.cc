#include <iostream>
#include <stdio.h>
#include <random>
#include <chrono>

using std::swap; 
using std::cout; 

int partition(int arr[], int low, int high) {
    int pivot = arr[high]; 
    int from_left = low; 
    int from_right = high - 1; 
    while (true) {
        while (arr[from_left] < pivot) {
            from_left++;
        }; 
        while (from_right > 0 && arr[from_right] > pivot) {
            from_right--; 
        }; 
        if (from_left >= from_right) break; 
        swap(arr[from_left], arr[from_right]); 
    }
    swap(arr[from_left], arr[high]); 
    return from_left; 
}


int quicksort(int arr[], int low, int high) {
    if (high <= low) return high; 
    int pivot = partition(arr, low, high);
    quicksort(arr, low, pivot - 1);
    quicksort(arr, pivot, high); 
    return 0; 
}


int main() {
    int arr[1000000];
    for (int i = 0; i < sizeof(arr)/sizeof(int); i++ ) {
        arr[i] = i; 
    }
    // Randomizing list 
    std::random_device rd; 
    std::mt19937 g(rd()); 
    std::shuffle(std::begin(arr), std::end(arr), g); 

    auto t1 = std::chrono::high_resolution_clock::now(); 
    quicksort(arr, 0, sizeof(arr)/sizeof(int) - 1); 
    auto t2 = std::chrono::high_resolution_clock::now(); 

    auto ms_int = std::chrono::duration_cast<std::chrono::milliseconds>(t2 - t1); 
    cout << ms_int.count() << "ms" << std::endl; 


    return 0; 
}
