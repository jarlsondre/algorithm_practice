import timeit
from random import sample
from numba import jit

#@jit(nopython=True)
def partition(arr, low, high):
    # Choosing the last element as pivot
    pivot = arr[high]
    from_right = high - 1 # Initial index 
    from_left = low

    while True: 
        while arr[from_left] < pivot: # moving in from the left
            from_left += 1
        while arr[from_right] > pivot and from_right > 0: #moving in from the right
            from_right -= 1
        if from_left >= from_right:
            break
        else: 
            arr[from_left], arr[from_right] = arr[from_right], arr[from_left] # swapping
    arr[from_left], arr[high] = arr[high], arr[from_left] # putting the pivot element in the middle, from the end of the array
    return from_left


#@jit(nopython=True)
def quicksort(arr, low, high): 
    if high <= low:
        return
    pivot = partition(arr, low, high)
    quicksort(arr, low, pivot - 1) 
    quicksort(arr, pivot, high)


integers = [*range(1000000)]
random_integers = sample(integers, len(integers))
integers2 = [*range(1000000)]
random_integers2 = sample(integers, len(integers))

def main():
    quicksort(random_integers2[0:100], 0, len(random_integers[0:100]) - 1)
    print(f"{random_integers[0:100]}")
    time = timeit.timeit('quicksort(random_integers, 0, len(random_integers) - 1)', 'from __main__ import quicksort, random_integers', number=1)
    print(f"time was: {time}")
    


if __name__ == "__main__":
    main()




