# Soal: Buat tampilan angka berikut : 1 2 4 7 8 10 13 14 16 19 20 22 25 , => n+1,n+2,n+3,...
# Penjelasan: Deret dengan penambahan yang berputar 1,2,3
# Asumsi: 13 angka pertama, langkah berulang 1,2,3

angka = 1
jumlah = 13
langkah = 1
for i in range(jumlah):
    print(angka, end=" ")
    angka = angka + langkah
    langkah = langkah + 1
    if langkah > 3:
        langkah = 1
print()
