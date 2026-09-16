# Soal: Tampilkan formasi bintang 2

# Perulangan untuk membuat 6 baris
for i in range(1, 7):

    # Membuat spasi di sebelah kiri
    spasi = 6 - i

    # Membuat jumlah bintang
    bintang = 2 * i - 1

    print(" " * spasi + "*" * bintang)