def missingNumber(arr, n):
    # O(n^2)
    # for i in range(1,n):
    #     if i in arr:
    #         continue
    #     else:
    #         return i

    # O(N)
    sum = (n*(n+1))/2
    arr_sum = 0

    for i in arr:
        arr_sum += i
    return int(sum - arr_sum)

# arr = [1,2, 3, 4]
arr = [6,1,2,8,3,4,7,9,5]
n = 10
print(missingNumber(arr, n))
