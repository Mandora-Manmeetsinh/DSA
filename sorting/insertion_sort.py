def print_array(arr):
  for element in arr:
    print(element, end=" ")
  print()

def insertion_sort(arr):
  for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1

    while j >= 0 and arr[j] > key:
      arr[j + 1] = arr[j]
      j -= 1
    arr[j + 1] = key

arr = [12, 54, 65, 7, 23, 9]
print_array(arr)
insertion_sort(arr)
print_array(arr)