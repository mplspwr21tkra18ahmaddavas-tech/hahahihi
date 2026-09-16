# Soal: Program menampilkan bilangan yang habis dibagi 6 dari n_awal hingga n_akhir
# Penjelasan: Menampilkan bilangan habis dibagi 6
# Asumsi: Termasuk batas

awal = int(input("Masukkan awal: "))
akhir = int(input("Masukkan akhir: "))

for i in range(awal, akhir + 1):
    if i % 6 == 0:
        print(i, end=" ")
print()
