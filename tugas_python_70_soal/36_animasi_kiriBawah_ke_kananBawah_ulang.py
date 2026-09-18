import time

lebar = 20

for i in range(5):
    print()

for ulang in range(2):
    for posisi in range(lebar):
        baris = ""
        for i in range(lebar):
            if i == posisi:
                baris = baris + "0"
            else:
                baris = baris + " "
        print(baris, end="\r")
        time.sleep(0.1)
    print()
