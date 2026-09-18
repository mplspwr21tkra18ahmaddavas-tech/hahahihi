n = int(input("Masukkan angka: "))

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
