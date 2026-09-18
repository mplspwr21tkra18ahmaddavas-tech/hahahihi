awal = int(input("Masukkan awal: "))
akhir = int(input("Masukkan akhir: "))

for i in range(awal, akhir + 1):
    if i % 6 == 0:
        print(i, end=" ")
print()
