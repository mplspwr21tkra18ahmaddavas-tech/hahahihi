# Soal: Buat tampilan angka berikut : 112333123455555123456
# Penjelasan: Pola selang-seling, ganjil diulang, genap menampilkan 1..i
# Asumsi: i ganjil -> tampilkan i sebanyak i kali, i genap -> tampilkan 1..i. n=1..6

for i in range(1, 7):
    if i % 2 == 1:
        # Ganjil: ulang angka i sebanyak i kali
        for j in range(i):
            print(i, end="")
    else:
        # Genap: tampilkan 1 sampai i
        for j in range(1, i + 1):
            print(j, end="")
print()
