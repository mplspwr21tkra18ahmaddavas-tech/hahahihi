# Soal: Buat tampilan angka berikut : 654321555554321333211
# Penjelasan: Versi menurun dari soal 8, i ganjil diulang, genap menampilkan i..1
# Asumsi: Untuk i=6 sampai 1, ganjil diulang, genap menampilkan i..1 menurun

for i in range(6, 0, -1):
    if i % 2 == 1:
        for j in range(i):
            print(i, end="")
    else:
        for j in range(i, 0, -1):
            print(j, end="")
print()
