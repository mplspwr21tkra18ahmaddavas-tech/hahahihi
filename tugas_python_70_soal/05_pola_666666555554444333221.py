# Soal: Buat tampilan angka berikut : 666666555554444333221
# Penjelasan: Kebalikan dari soal 4, menampilkan 6 sebanyak 6 kali sampai 1 sebanyak 1 kali
# Asumsi: Pola untuk n=6 sampai 1

# Perulangan dari 6 sampai 1
for i in range(6, 0, -1):
    for j in range(i):
        print(i, end="")
print()
