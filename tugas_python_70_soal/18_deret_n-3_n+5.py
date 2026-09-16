# Soal: Buat tampilan angka berikut : 5 2 7 4 9 6 11 8 13 10 15 12 , => n-3,n+5,...
# Penjelasan: Deret selang-seling -3 dan +5
# Asumsi: 12 angka pertama

angka = 5
jumlah = 12
for i in range(jumlah):
    print(angka, end=" ")
    if i % 2 == 0:
        angka = angka - 3
    else:
        angka = angka + 5
print()
