# Soal: Buat tampilan angka berikut : 122123444412345666666
# Penjelasan: Kebalikan soal 8, genap diulang, ganjil menampilkan 1..i
# Asumsi: i genap -> ulang i sebanyak i kali, i ganjil -> tampilkan 1..i. n=1..6

for i in range(1, 7):
    if i % 2 == 0:
        for j in range(i):
            print(i, end="")
    else:
        for j in range(1, i + 1):
            print(j, end="")
print()
