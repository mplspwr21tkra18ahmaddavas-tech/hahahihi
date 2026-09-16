# Soal: Buat tampilan angka berikut : 122123123455555666666123456712345678999999999...
# Penjelasan: Pola sama seperti soal 9 (genap diulang, ganjil berurutan) diperpanjang sampai 9
# Asumsi: Tanda ... artinya dilanjutkan sampai 9, aturan genap diulang ganjil 1..i

for i in range(1, 10):
    if i % 2 == 0:
        for j in range(i):
            print(i, end="")
    else:
        for j in range(1, i + 1):
            print(j, end="")
print()
