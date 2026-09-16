# Soal: Buat tampilan angka berikut : 112123123412345123456
# Penjelasan: Menampilkan 1, lalu 12, lalu 123, sampai 123456 digabungkan
# Asumsi: Pola untuk n=1 sampai 6, tiap bagian menampilkan 1 sampai i

for i in range(1, 7):
    for j in range(1, i + 1):
        print(j, end="")
print()
