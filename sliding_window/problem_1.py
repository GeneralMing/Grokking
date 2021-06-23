# Given an array of positive numbers and a positive number ‘k,’ find the maximum sum of any contiguous subarray of size ‘k’.
def max_sub_array_of_size_k(k, arr):
    total = sum(arr[:k])
    sums = [total]
    arrays = [arr[:k]]
    for i in range(k, len(arr)):
        total += arr[i]
        total -= arr[i-k]
        sums.append(total)
        arrays.append(arr[i-k+1:i+1])
    return arrays[sums.index(max(sums))]

print(max_sub_array_of_size_k(3, [2,1,5,1,3,2]))
print(max_sub_array_of_size_k(2, [2,3,4,1,5]))
