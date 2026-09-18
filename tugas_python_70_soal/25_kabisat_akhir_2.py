awal = int(input("Masukkan tahun awal: "))
akhir = int(input("Masukkan tahun akhir: "))

for tahun in range(awal, akhir + 1):
    if tahun % 4 == 0 and tahun % 10 == 2:
        print(tahun, end=" ")
print()
