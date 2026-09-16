# Soal: Program menampilkan bilangan yang habis dibagi 7 dari n_awal hingga n_akhir
# Penjelasan: Menampilkan bilangan habis dibagi 7
# Asumsi: Termasuk batas

awal = int(input("Masukkan awal: "))
akhir = int(input("Masukkan akhir: "))

for i in range(awal, akhir + 1):
    if i % 7 == 0:
        print(i, end=" ")
print()
