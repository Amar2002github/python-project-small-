#Sum of Non-Divisible Numbers


def sum_numbers(m, n):
    divisible = 0
    non_divisible = 0

    for i in range(1, n + 1):

        
        if i % m == 0:
            divisible += i
        else:
            non_divisible += i

    return non_divisible, divisible


m = 3
n = 10

a, b = sum_numbers(m, n)

print("Non-divisible sum:", a)
print("Divisible sum:", b)