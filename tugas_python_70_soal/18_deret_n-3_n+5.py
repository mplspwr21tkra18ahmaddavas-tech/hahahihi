angka = 5
jumlah = 12
for i in range(jumlah):
    print(angka, end=" ")
    if i % 2 == 0:
        angka = angka - 3
    else:
        angka = angka + 5
print()
