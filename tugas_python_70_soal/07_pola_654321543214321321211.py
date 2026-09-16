# Soal: Buat tampilan angka berikut : 654321543214321321211
# Penjelasan: Kebalikan soal 6, menampilkan 654321, 54321, 4321, 321, 21, 1
# Asumsi: Pola untuk n=6 sampai 1, tiap bagian menampilkan i sampai 1

for i in range(6, 0, -1):
    for j in range(i, 0, -1):
        print(j, end="")
print()
