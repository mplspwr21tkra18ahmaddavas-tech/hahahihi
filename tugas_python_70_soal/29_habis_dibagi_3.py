awal = int(input("Masukkan awal: "))
akhir = int(input("Masukkan akhir: "))

for i in range(awal, akhir + 1):
    if i % 3 == 0:
        print(i, end=" ")
print()
