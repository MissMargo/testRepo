def my_sum(numbers):
    x = 0
    while numbers > 0:
        x += numbers % 10
        numbers //= 10
    return x


a = int(input("Enter numbers: "))
result = my_sum(a)
print(result)
