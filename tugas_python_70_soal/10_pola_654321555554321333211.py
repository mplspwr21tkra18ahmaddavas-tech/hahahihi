for i in range(6, 0, -1):
    if i % 2 == 1:
        for j in range(i):
            print(i, end="")
    else:
        for j in range(i, 0, -1):
            print(j, end="")
print()
