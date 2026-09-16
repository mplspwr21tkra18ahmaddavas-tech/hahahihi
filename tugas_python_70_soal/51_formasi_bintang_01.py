# Soal: Tampilkan formasi bintang 1

# Perulangan untuk membuat 6 baris
for i in range(6):

    if i == 0:
        # Baris pertama penuh
        print("*" * 11)
    else:
        # Jumlah bintang kiri dan kanan
        bintang = 6 - i

        # Jumlah spasi di tengah
        spasi = 2 * i - 1

        print("*" * bintang + " " * spasi + "*" * bintang)