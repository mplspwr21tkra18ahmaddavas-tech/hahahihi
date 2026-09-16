# Soal: Buat tampilan angka berikut : 876543217654321666666555554321321221
# Penjelasan: Pola menurun lainnya dengan kombinasi angka berulang dan menurun
# Asumsi: Untuk i=8..1 dengan kombinasi, agar hasil mendekati contoh soal

# Contoh pola: 87654321 7654321 666666 55555 4321 321 22 1 (mendekati contoh)
for i in range(8, 0, -1):
    if i == 6 or i == 5 or i == 2:
        for j in range(i):
            print(i, end="")
    else:
        for j in range(i, 0, -1):
            print(j, end="")
print()
