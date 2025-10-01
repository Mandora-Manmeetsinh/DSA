# Medium Problems relreted to array in the perspective of DSA :- 
# 1. Array Rotation
# 2. Array Reversal
# 3. Array Pair Sum
# 4. Array Subarray Sum
# 5. Array Subarray Product
# 6. Array Subarray Min/Max

# Answer :- 

# 1. Array Rotation :- 
# Problem Statement :- Given an array of integers and a number of positions to rotate the array, rotate the array to the right by that number of positions.

numbers = [1, 2, 3, 4, 5, 6, 7]
k = 3

def rotate_array(numbers, k) :
    k = k % len(numbers)
    numbers[:] = numbers[-k:] + numbers[:-k]
    return numbers

print(rotate_array(numbers, k))
# Output :- [5, 6, 7, 1, 2, 3, 4]

# 2. Array Reversal :-

numbers2 = [1,2,3,4,5]

def arr_rev(numbers2) :
    return numbers2[::-1]

print(arr_rev(numbers2))
# Output :- [5, 4, 3, 2, 1]

# 3. Array Pair Sum :-

numbers3 = [1, 2, 3, 4, 5]

def pair_sum(numbers3) :
    pairs = []
    for i in range(len(numbers3)) :
        for j in range(i + 1, len(numbers3)) :
            pairs.append(numbers3[i] + numbers3[j])
            return pairs

print(pair_sum(numbers3))
# Output :- [5, 5, 7]