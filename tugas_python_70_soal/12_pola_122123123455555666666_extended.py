for i in range(1, 10):
    if i % 2 == 0:
        for j in range(i):
            print(i, end="")
    else:
        for j in range(1, i + 1):
            print(j, end="")
print()
