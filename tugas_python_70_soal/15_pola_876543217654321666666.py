for i in range(8, 0, -1):
    if i == 6 or i == 5 or i == 2:
        for j in range(i):
            print(i, end="")
    else:
        for j in range(i, 0, -1):
            print(j, end="")
print()
