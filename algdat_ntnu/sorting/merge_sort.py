
import random
import timeit

def merge(arr, left, mid, right):

  # ------------------------------
  # This seems to be really slow, and the reason
  # for this, I would think, is because the function 
  # copies a lot of lists 
  # ------------------------------

  arr1 = arr[left:mid+1]
  arr2 = arr[mid+1:right+1]
  temp_arr = []
  len_arr1 = len(arr1)
  len_arr2 = len(arr2)
  while len_arr1 > 0 or len_arr2 > 0:
    if len_arr2 == 0:
      temp_arr.append(arr1.pop(0))
      len_arr1 -= 1
    elif len_arr1 == 0:
      temp_arr.append(arr2.pop(0))
      len_arr2 -= 1
    elif arr1[0] < arr2[0]:
      temp_arr.append(arr1.pop(0))
      len_arr1 -= 1
    else:
      temp_arr.append(arr2.pop(0))
      len_arr2 -= 1
  for i in range(len(temp_arr)):
    arr[left + i] = temp_arr[i]



def merge_sort(arr, left, right):
  if right <= left:
    return
  mid = int((right + left)/2) 
  merge_sort(arr, left, mid) 
  merge_sort(arr, mid + 1, right)
  merge(arr, left, mid, right)

 

integers = [*range(300000)]
random_integers = random.sample(integers, len(integers))
random_integers_sorted = sorted(random_integers)

def main():
  time = timeit.timeit('merge_sort(random_integers, 0, len(random_integers) - 1)', 'from __main__ import merge_sort, random_integers', number=1)
  print(f"time was: {time}")


if __name__ == "__main__":
	main()
