def rotate(arr, n):
    last = arr[-1]
    arr.insert(0,last)
    arr.pop()
    return arr
A = [1, 2, 3, 4, 5]
N = len(A)
print(rotate(A,N))
