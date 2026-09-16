# Soal: Buat tampilan angka berikut : 2 12 7 17 12 22 17 27 22 32 , => n+10,n-5,...
# Penjelasan: Deret selang-seling +10 dan -5
# Asumsi: 10 angka pertama

angka = 2
jumlah = 10
for i in range(jumlah):
    print(angka, end=" ")
    if i % 2 == 0:
        angka = angka + 10
    else:
        angka = angka - 5
print()
