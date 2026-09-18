print("Masukkan 10 angka:")

angka = int(input("Masukkan angka ke-1: "))
terkecil = angka

for i in range(2, 11):
    angka = int(input("Masukkan angka ke-" + str(i) + ": "))
    if angka < terkecil:
        terkecil = angka

print("Bilangan terkecil adalah: " + str(terkecil))
