# Find Maximum and Minimum:

# Write a function that takes an array of integers as input and returns the maximum and minimum elements in the array.
# What is the time complexity of your solution?

def find_max_min(arr):
    if not arr:
        return None, None  

    max_val = arr[0]
    min_val = arr[0]

    for num in arr:
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num

    return max_val, min_val 

# time complexity = "O(n)" 

# Calculate Sum of Elements:
# Write a function that takes an array of integers and returns the sum of all its elements.
# What is the time complexity? (You already discussed this, but implement it!)

def sum_of_elements(arr):
    total = 0
    for num in arr:
        total += num
    return total

# time complexity = "O(n)"

# Reverse an Array:
# Write a function that takes an array and reverses its elements in-place (without creating a new array, if possible, for optimal space).
# Example: [1, 2, 3, 4, 5] becomes [5, 4, 3, 2, 1]
# What is the time complexity?
def reverse_array(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]  # Swap elements
        left += 1
        right -= 1

    return arr

# time complexity = "O(n)"

# Search for an Element:
# Write a function that takes an array and a target value. It should return the index of the target value if found, otherwise return -1.
# What is the time complexity? (This is linear search)
def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1

# time complexity = "O(n)"

# 2D Array Sum (Optional but Recommended):
# Write a function that takes a 2D array (matrix) of integers and returns the sum of all its elements.
# What is the time complexity?
def sum_2d_array(matrix):
    total = 0
    for row in matrix:
        for num in row:
            total += num
    return total

# time complexity = "O(m * n)" 