# Soal: Tampilkan bilangan Faktorial dari n! dan hasilnya => 3! = 3 x 2 x 1 = 6
# Penjelasan: Meminta n lalu menghitung faktorial dan menampilkan prosesnya
# Asumsi: n adalah bilangan bulat positif

# Memasukkan angka
n = int(input("Masukkan angka: "))

# Menghitung faktorial
hasil = 1
for i in range(1, n + 1):
    hasil = hasil * i

# Menampilkan proses
print(str(n) + "! = ", end="")
for i in range(n, 0, -1):
    print(i, end="")
    if i != 1:
        print(" x ", end="")
print(" = " + str(hasil))
