def even_odd_sum(arr):
    even = arr[0::2]
    odd = arr[1::2]

    even.sort()
    odd.sort()

    return even[-2] + odd[1]


arr = [10, 20, 30, 40, 50, 60]
print(even_odd_sum(arr))