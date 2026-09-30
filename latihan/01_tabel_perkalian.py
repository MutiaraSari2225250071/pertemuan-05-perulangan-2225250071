# Input: bilangan bulat n
# Proses: perulangan for dari 1 sampai 10
# Output: tabel perkalian n

n = int(input("Bilangan: "))

for i in range(1, 11):
    hasil = n * i
    print(f"{n} x {i} = {hasil}")