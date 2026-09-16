# Soal: Buat tampilan angka berikut : 666666123454444123221
# Penjelasan: Kebalikan dari soal 9, dari 6 sampai 1 dengan aturan genap diulang ganjil berurutan
# Asumsi: Untuk i=6 sampai 1, jika genap tampilkan i sebanyak i kali, jika ganjil tampilkan 1..i

for i in range(6, 0, -1):
    if i % 2 == 0:
        for j in range(i):
            print(i, end="")
    else:
        for j in range(1, i + 1):
            print(j, end="")
print()
