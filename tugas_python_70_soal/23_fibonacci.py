# Soal: Buat Program untuk menampilkan bilangan Fibonacci -> 0,1,1,2,3,5,8,13,21,34,... dengan nilai maksimum ditentukan
# Penjelasan: Meminta batas maksimum lalu menampilkan deret Fibonacci sampai batas tersebut
# Asumsi: Batas adalah nilai maksimum, bukan jumlah bilangan

# Memasukkan batas maksimum
batas = int(input("Masukkan batas maksimum: "))

# Menampilkan Fibonacci
a = 0
b = 1
print(a, end=" ")
print(b, end=" ")
while True:
    c = a + b
    if c > batas:
        break
    print(c, end=" ")
    a = b
    b = c
print()
