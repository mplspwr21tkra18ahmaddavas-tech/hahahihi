import time

tinggi = 10

for ulang in range(2):
    for posisi in range(tinggi):
        for i in range(tinggi):
            if i == posisi:
                print("0")
            else:
                print()
        time.sleep(0.2)
        if posisi != tinggi - 1:
            for k in range(5):
                print()
