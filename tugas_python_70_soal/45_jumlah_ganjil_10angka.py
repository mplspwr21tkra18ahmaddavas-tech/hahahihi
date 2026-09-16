# Soal: Masukkan beberapa angka (min 10) dengan looping, kemudian hitung jumlah bilangan ganjil dari beberapa masukan tersebut
# Penjelasan: Menghitung bilangan ganjil dari 10 angka
# Asumsi: 10 angka

print("Masukkan 10 angka:")

jumlah_ganjil = 0
for i in range(1, 11):
    angka = int(input("Masukkan angka ke-" + str(i) + ": "))
    if angka % 2 == 1:
        jumlah_ganjil = jumlah_ganjil + 1

print("Jumlah bilangan ganjil: " + str(jumlah_ganjil))
