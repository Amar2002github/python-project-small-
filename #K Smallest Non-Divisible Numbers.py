#K Smallest Non-Divisible Numbers

def k_smallest_non_divisible(arr, k):
    result = []
    num = 1

    while len(result) < k:
        valid = True

        for x in arr:
            if num % x == 0:
                valid = False
                break

        if valid:
            result.append(num)

        num += 1

    return sum(result)


arr = [2, 3]
k = 4
print(k_smallest_non_divisible(arr, k))