a = input('Enter a word: ')
reverse = a[::-1]
def palindrom (a):
    if a[::1] == reverse:
        return True
    else:
        return False

print(palindrom(a))

#or
n = lambda a: True if a[::1] == reverse else False
print(n(a))
