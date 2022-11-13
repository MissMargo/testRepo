def season(month):
    if month == 12 or month == 1 or month == 2:
        return ('Зима')
    if month == 3 or month == 4 or month == 5:
        return ('Весна')
    if month == 6 or month == 7 or month == 8:
        return ('Літо')
    if month == 9 or month == 10 or month == 11:
        return ('Осінь')

time_of_the_year = season (int(input('Введіть номер місяця: ')))
print(time_of_the_year)

