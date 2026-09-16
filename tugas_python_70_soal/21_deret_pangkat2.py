# Soal: Buat tampilan angka berikut : 1 2 4 8 16 32 64 128 256 512
# Penjelasan: Deret pangkat 2
# Asumsi: 10 angka pertama

angka = 1
for i in range(10):
    print(angka, end=" ")
    angka = angka * 2
print()
