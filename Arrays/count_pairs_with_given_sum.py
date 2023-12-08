def getPairsCount(arr, k):
    # count = 0
    # for i in range(n):
    #     for j in range(i + 1, n):
    #         if arr[i] + arr[j] == k:
    #             count += 1
    # return count
    unordered_map = {}
    count = 0
    n = len(arr)
    for i in range(n):
        if k - arr[i] in unordered_map:
            count += unordered_map[k - arr[i]]
        if arr[i] in unordered_map:
            unordered_map[arr[i]] += 1
        else:
            unordered_map[arr[i]] = 1
    return count


k = 10
# arr = [1, 5, 7, 1]
# arr = [1, 1, 1, 1]
arr = [1, 5, 5, 5, 5, 7]
print(getPairsCount(arr, k))
