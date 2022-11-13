f1 = 1
f2 = 1

i = int(input())

print(f1, f2)
while i > 2:
  f1, f2 = f2, f1 + f2
  print(f2)
  i -= 1
