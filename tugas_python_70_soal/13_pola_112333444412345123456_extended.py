# Soal: Buat tampilan angka berikut : 112333444412345123456777777788888888123456789...
# Penjelasan: Pola sama seperti soal 8 (ganjil diulang, genap berurutan) diperpanjang sampai 9
# Asumsi: Tanda ... artinya sampai 9, ganjil diulang ganjil kali, genap tampil 1..i

for i in range(1, 10):
    if i % 2 == 1:
        for j in range(i):
            print(i, end="")
    else:
        for j in range(1, i + 1):
            print(j, end="")
print()
