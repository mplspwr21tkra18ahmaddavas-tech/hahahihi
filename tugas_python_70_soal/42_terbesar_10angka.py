# Soal: Masukkan beberapa angka (min 10) dengan looping, kemudian cari bilangan terbesar dari beberapa masukan tersebut
# Penjelasan: Meminta 10 angka lalu mencari yang terbesar
# Asumsi: Minimal 10 angka, pengguna memasukkan 10 angka

# Meminta jumlah angka
print("Masukkan 10 angka:")

# Input angka pertama sebagai terbesar awal
angka = int(input("Masukkan angka ke-1: "))
terbesar = angka

# Perulangan untuk 9 angka berikutnya
for i in range(2, 11):
    angka = int(input("Masukkan angka ke-" + str(i) + ": "))
    if angka > terbesar:
        terbesar = angka

# Menampilkan hasil
print("Bilangan terbesar adalah: " + str(terbesar))
