# Soal: Tampilkan formasi bintang 5

# Perulangan untuk membuat 6 baris
for i in range(6):

    # Spasi di sebelah kiri bertambah
    spasi = i

    # Bintang berkurang 2 setiap baris
    bintang = 11 - (2 * i)

    print(" " * spasi + "*" * bintang)