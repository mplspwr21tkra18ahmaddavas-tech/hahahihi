for i in range(1, 6):

    if i == 5:
        print("*" * 11)
    else:
        bintang = i

        spasi = 9 - (2 * (i - 1))

        print("*" * bintang + " " * spasi + "*" * bintang)