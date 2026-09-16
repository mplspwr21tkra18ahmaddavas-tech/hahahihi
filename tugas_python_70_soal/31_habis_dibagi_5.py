# Soal: Program menampilkan bilangan yang habis dibagi 5 dari n_awal hingga n_akhir
# Penjelasan: Menampilkan bilangan habis dibagi 5
# Asumsi: Termasuk batas

awal = int(input("Masukkan awal: "))
akhir = int(input("Masukkan akhir: "))

for i in range(awal, akhir + 1):
    if i % 5 == 0:
        print(i, end=" ")
print()
