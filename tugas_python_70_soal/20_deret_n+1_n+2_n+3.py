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
