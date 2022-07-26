import random

def merge(arr, left, mid, right):
  arr1 = arr[left:mid+1]
  arr2 = arr[mid+1:right+1]
  temp_arr = []
  while len(arr1) > 0 or len(arr2) > 0:
    if len(arr2) == 0:
      temp_arr.append(arr1.pop(0))
    elif len(arr1) == 0:
      temp_arr.append(arr2.pop(0))
    elif arr1[0] < arr2[0]:
      temp_arr.append(arr1.pop(0))
    else:
      temp_arr.append(arr2.pop(0))
  for i in range(len(temp_arr)):
    arr[left + i] = temp_arr[i]



def merge_sort(arr, left, right):
  if right <= left:
    return
  mid = int((right + left)/2) 
  merge_sort(arr, left, mid) 
  merge_sort(arr, mid + 1, right)
  merge(arr, left, mid, right)

 


def main():
  integers = [*range(1000)]
  random_integers = random.choices(integers, k=1000)
  random_integers_sorted = sorted(random_integers)
  merge_sort(random_integers, 0, len(random_integers) - 1)
  print(f"sorting...")
  if random_integers_sorted == random_integers:
    print(f"successfully sorted the list")
  else:
    print(f"failed to sort the list")


if __name__ == "__main__":
	main()
