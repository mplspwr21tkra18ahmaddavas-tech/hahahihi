# Soal: Tampilkan formasi bintang 4

# Perulangan untuk membuat 5 baris
for i in range(1, 6):

    if i == 5:
        # Baris terakhir penuh
        print("*" * 11)
    else:
        # Jumlah bintang di kiri dan kanan
        bintang = i

        # Spasi di tengah semakin sedikit
        spasi = 9 - (2 * (i - 1))

        print("*" * bintang + " " * spasi + "*" * bintang)