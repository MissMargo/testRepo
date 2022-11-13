def tri_recursion(k):
    if k > 0:
        print(k)
    tri_recursion(k - 1)


print("\n\nRecursion Example Results")
tri_recursion(int(input("Введіть число: ")))




