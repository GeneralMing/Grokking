# Given an array, find the average of all contiguous subarrays of size ‘K’ in it.
def find_average_of_subarrays(K, arr):
    avg = sum(arr[:K])/K
    result = [avg] 
    for i in range(K, len(arr)):
        avg += arr[i]/K
        avg -= arr[i-K]/K
        result.append(avg)
    return result

print(find_average_of_subarrays(5, [1,3,2,6,-1,4,1,8,2]))
