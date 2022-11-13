import math
my_list = []

for num in range(10):
    x = int(input('Введіть ціле чісло: '))
    my_list.append(x)
    print(my_list)
    result = (sum(my_list))

print(result)