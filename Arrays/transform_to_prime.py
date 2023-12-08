def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def min_number(arr):
    total_sum = 0
    for i in arr:
        total_sum += i
    required = 0

    while not is_prime(total_sum + required):
        required += 1
    return required


arr = [1, 5, 7]
n = len(arr)
# print(min_number_to_insert(arr))
print(min_number(arr))
