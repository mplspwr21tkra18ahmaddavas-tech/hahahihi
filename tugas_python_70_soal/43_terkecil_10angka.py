# Soal: Masukkan beberapa angka (min 10) dengan looping, kemudian cari bilangan terkecil dari beberapa masukan tersebut
# Penjelasan: Sama seperti soal 42 tapi mencari terkecil
# Asumsi: 10 angka

print("Masukkan 10 angka:")

angka = int(input("Masukkan angka ke-1: "))
terkecil = angka

for i in range(2, 11):
    angka = int(input("Masukkan angka ke-" + str(i) + ": "))
    if angka < terkecil:
        terkecil = angka

print("Bilangan terkecil adalah: " + str(terkecil))
