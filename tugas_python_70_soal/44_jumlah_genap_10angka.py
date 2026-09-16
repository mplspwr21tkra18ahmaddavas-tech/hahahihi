# Soal: Masukkan beberapa angka (min 10) dengan looping, kemudian hitung jumlah bilangan genap dari beberapa masukan tersebut
# Penjelasan: Menghitung berapa banyak bilangan genap dari 10 angka
# Asumsi: 10 angka

print("Masukkan 10 angka:")

jumlah_genap = 0
for i in range(1, 11):
    angka = int(input("Masukkan angka ke-" + str(i) + ": "))
    if angka % 2 == 0:
        jumlah_genap = jumlah_genap + 1

print("Jumlah bilangan genap: " + str(jumlah_genap))
