def minNumber(arr, n):
    sum = 0
    min_num = 0

    for i in arr:
        sum += i
    

arr = [2, 4, 6, 8, 12]
n = len(arr)
print(minNumber(arr,n))