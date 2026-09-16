# Soal: Buat tampilan angka berikut : 3 9 4 12 7 21 16 48 43 129 , => n*3,n-5,...
# Penjelasan: Deret selang-seling *3 dan -5
# Asumsi: 10 angka pertama

angka = 3
jumlah = 10
for i in range(jumlah):
    print(angka, end=" ")
    if i % 2 == 0:
        angka = angka * 3
    else:
        angka = angka - 5
print()
