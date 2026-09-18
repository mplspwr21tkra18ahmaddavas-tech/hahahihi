for i in range(6, 0, -1):
    spasi = " " * (6 - i)

    if i == 4:
        bintang = "***"
    elif i == 2:
        bintang = "**"
    else:
        bintang = "*" * i

    print(spasi + "*" * i)
for i in range(2, 6):
    spasi = " " * (6 - i)
    print(spasi + "*" * i)
