angka = 2
jumlah = 10
for i in range(jumlah):
    print(angka, end=" ")
    if i % 2 == 0:
        angka = angka + 10
    else:
        angka = angka - 5
print()
