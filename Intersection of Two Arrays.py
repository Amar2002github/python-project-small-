def intersection(arr1, arr2):
    set1 = set(arr1)
    set2 = set(arr2)

    return list(set1 & set2)


a = [1, 2, 2, 3, 4]
b = [2, 2, 4, 5]

print(intersection(a, b))
