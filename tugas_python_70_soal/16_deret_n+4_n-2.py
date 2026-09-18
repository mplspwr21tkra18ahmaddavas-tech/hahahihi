angka = 1

jumlah = 12
for i in range(jumlah):
    print(angka, end=" ")
    if i % 2 == 0:
        angka = angka + 4
    else:
        angka = angka - 2
print()
