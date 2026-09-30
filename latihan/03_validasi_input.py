# Input: nilai ujian 0 sampai 100
# Proses: validasi input dengan while sampai nilai berada dalam rentang
# Output: nilai yang diterima

nilai = float(input("Nilai 0-100: "))

while nilai < 0 or nilai > 100:
    print("Nilai tidak valid.")
    nilai = float(input("Nilai 0-100: "))

print(f"Nilai diterima: {nilai}")