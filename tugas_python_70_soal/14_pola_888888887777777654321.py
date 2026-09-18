for i in range(8, 0, -1):
    if i == 8 or i == 7 or i == 4 or i == 3:
        for j in range(i):
            print(i, end="")
    else:
        for j in range(i, 0, -1):
            print(j, end="")
print()
