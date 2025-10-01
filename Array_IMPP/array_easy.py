# Easy Problems relreted to array in the perspective of DSA :- 
# 1. Find the maximum element in an array
# 2. Find the minimum element in an array
# 3. Find the sum of all elements in an array
# 4. Find the average of all elements in an array
# 5. Find the maximum and minimum element in an array
# 6. Find the second maximum and second minimum element in an array
# 7. Find the first and last occurrence of an element in an array
# 8. Find the maximum and minimum element in a subarray of an array

# Answer :- 

# 1. Find the maximum element in an array

numbers = [1,2,3,4,5,6,7,8,9,2,3,4,5]

def max_num(numbers) :
    return max(numbers)

print(max_num(numbers))

# without importing max function

def max_num_manual(numbers):
    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value

print(max_num_manual(numbers))

# Output: 9
# Time Complexity: O(n) where n is the number of elements in the array.
# Space Complexity: O(1) as we are not using any extra space.

# 2. Find the minimum element in an array

numbers1 = [1,2,3,4,5,6,7,8,9]

def min_num(numbers1) :
    return min(numbers1)

print(min_num(numbers1))
# Output: 1
# Time Complexity: O(n) where n is the number of elements in the array.
# Space Complexity: O(1) as we are not using any extra space.

# 3. Find the sum of all elements in an array

numbers3 = [1,2,3,4,5]

def sum_num(numbers3) :
    return sum(numbers3)

print(sum_num(numbers3))
# Output: 15
# Time Complexity: O(n) where n is the number of elements in the array.
# Space Complexity: O(1) as we are not using any extra space.

# 4. Find the average of all elements in an array

numbers4 = [1,2,3,4,5,6]

def avg_num(numbers4) :
    return sum(numbers4) / len(numbers4)

print(avg_num(numbers4))
# Output: 3.5
# Time Complexity: O(n) where n is the number of elements in the array.
# Space Complexity: O(1) as we are not using any extra space.

# 5. Find the maximum and minimum element in an array

numbers5 = [1,2,3,4,5,6,7]

def max_min_num(numbers5) :
    return max(numbers5), min(numbers5)

print(max_min_num(numbers5))
# Output: (7, 1)
# Time Complexity: O(n) where n is the number of elements in the array.
# Space Complexity: O(1) as we are not using any extra space.

# 6. Find the middle element of an array

numbers6 = [1,2,3,4,5,6,7]

def mid_num(numbers6) :
    n = len(numbers6)

    if n % 2 == 0 :
        return (numbers6[n // 2 - 1] + numbers6[n // 2]) / 2  
    else :
        return numbers6[n // 2]

print(mid_num(numbers6))
# Output: 4.0
# Time Complexity: O(n) where n is the number of elements in the array.
# Space Complexity: O(1) as we are not using any extra space.

# 7. Find the second maximum and second minimum element in an array

numbers7 = [1,3,6,5,4,7,2,6,4,1]

def sec_min_max(numbers7) :
    numbers7.sort()
    return numbers7[-2], numbers7[1]

print(sec_min_max(numbers7))
# Output: (4, 3)
# Time Complexity: O(n log n) where n is the number of elements in the array.
# Space Complexity: O(n) as we are sorting the array.

# 8. Find the first and last occurrence of an element in an array .

numbers8 = [1,2,3,4,1,4,5,2,3,6,4,7]

def first_last_occurrence(numbers8, target):
    try:
        first_occurrence = numbers8.index(target)
        last_occurrence = len(numbers8) - 1 - numbers8[::-1].index(target)
        return first_occurrence, last_occurrence
    except ValueError:
        return -1, -1

print(first_last_occurrence(numbers8, 4))
# Output: (3, 10)
# Time Complexity: O(n) where n is the number of elements in the array.
# Space Complexity: O(n) as we are using the index method which creates a new list in memory.

# 9. Find the maximum and minimum element in an array using recursion.

numbers9 = [1,2,3,4,5,6,7,8,9]

def max_min(numbers9, n):
    if n == 0:
        return numbers9[0], numbers9[0]
    else:
        max_val, min_val = max_min(numbers9, n-1)
        if numbers9[n] > max_val:
            return numbers9[n], min_val
        elif numbers9[n] < min_val:
            return max_val, numbers9[n]
        else:
            return max_val, min_val

print(max_min(numbers9, len(numbers9)-1))
# Output: (9, 1)
# Time Complexity: O(n) where n is the number of elements in the array.
# Space Complexity: O(n) as we are using recursion which creates a new stack frame for each recursive call.

# 10. Find the maximum and minimum element in an array using a stack.

numbers10 = [1,2,3,4,5,6,7,8,9]

def max_min_stack(numbers10):
    stack = []
    max_val = float('-inf')
    min_val = float('inf')
    for num in numbers10:
        while stack and stack[-1] < num:
            max_val = max(max_val, stack.pop())
            while stack and stack[-1] > num:
                min_val = min(min_val, stack.pop())
                stack.append(num)
                stack.append(num)
                return max_val, min_val

print(max_min_stack(numbers10))
# Output: (9, 1)
# Time Complexity: O(n) where n is the number of elements in the array.
# Space Complexity: O(n) as we are using a stack to store the elements.