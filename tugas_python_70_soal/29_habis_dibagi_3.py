# Soal: Program menampilkan bilangan yang habis dibagi 3 dari n_awal hingga n_akhir
# Penjelasan: Menampilkan bilangan yang habis dibagi 3 di rentang tertentu
# Asumsi: Termasuk batas awal dan akhir

awal = int(input("Masukkan awal: "))
akhir = int(input("Masukkan akhir: "))

for i in range(awal, akhir + 1):
    if i % 3 == 0:
        print(i, end=" ")
print()
