# Pertemuan 05 Perulangan Python

Nama: Mutiara Sari
NIM: 2225250071
Kelas: 3A
Program Studi: Pendidikan Matematika

## Tujuan

Pertemuan 05 bertujuan untuk mempelajari dan menerapkan perulangan `for` dan `while` dalam Python. Perulangan digunakan untuk menjalankan proses secara berulang sesuai jumlah iterasi atau kondisi tertentu. Pada pertemuan ini juga diterapkan validasi input, seleksi di dalam perulangan, akumulasi, serta pencacahan.

## Struktur Program

Program pada Pertemuan 05 terdiri atas empat latihan dan satu kuis.

```text
pertemuan-05-perulangan-2225250071/
│
├── README.md
├── .gitignore
│
├── latihan/
│   ├── 01_tabel_perkalian.py
│   ├── 02_jumlah_bilangan.py
│   ├── 03_validasi_input.py
│   └── 04_hitung_genap.py
│
└── kuis/
    └── kuis2_deret_aritmetika.py
```

## Cara Menjalankan

Program dapat dijalankan melalui Terminal VS Code dengan perintah berikut:

```text
python latihan/01_tabel_perkalian.py
python latihan/02_jumlah_bilangan.py
python latihan/03_validasi_input.py
python latihan/04_hitung_genap.py
python kuis/kuis2_deret_aritmetika.py
```

## Algoritma Kuis 2

Program Kuis 2 digunakan untuk menampilkan beberapa suku pertama deret aritmetika dan menghitung jumlah seluruh suku secara iteratif.

Langkah-langkah algoritmanya:

1. Memasukkan suku pertama `a` sebagai `float`.
2. Memasukkan beda `d` sebagai `float`.
3. Memasukkan banyak suku `n` sebagai `integer`.
4. Memvalidasi nilai `n` menggunakan `while`. Jika `n <= 0`, program meminta input kembali sampai mendapatkan nilai positif.
5. Menginisialisasi `total = 0`.
6. Menggunakan `for` untuk mengulang proses sebanyak `n` kali.
7. Menghitung setiap suku dengan rumus `suku = a + i * d`.
8. Menambahkan setiap suku ke dalam `total`.
9. Menampilkan nomor suku dan nilai setiap suku.
10. Setelah perulangan selesai, menampilkan jumlah seluruh suku dengan dua angka di belakang koma.

Pada Kuis 2, `while` digunakan untuk proses validasi karena proses bergantung pada kondisi input, sedangkan `for` digunakan untuk menghasilkan suku karena jumlah iterasi sudah diketahui dari nilai `n`.

## Hasil Pengujian

Seluruh program telah diuji menggunakan test case yang ditentukan pada modul Pertemuan 05.

| Program                     | Input                     | Keluaran yang Diharapkan                  | Keluaran Aktual                                                                    | Status   |
| --------------------------- | ------------------------- | ----------------------------------------- | ---------------------------------------------------------------------------------- | -------- |
| `01_tabel_perkalian.py`     | `n = 4`                   | Perkalian 4 dari ×1 sampai ×10            | 4 × 1 = 4 sampai 4 × 10 = 40                                                       | Berhasil |
| `01_tabel_perkalian.py`     | `n = -3`                  | Perkalian -3 dari ×1 sampai ×10           | -3 × 1 = -3 sampai -3 × 10 = -30                                                   | Berhasil |
| `02_jumlah_bilangan.py`     | `n = 1`                   | `Jumlah = 1`                              | `Jumlah = 1`                                                                       | Berhasil |
| `02_jumlah_bilangan.py`     | `n = 5`                   | `Jumlah = 15`                             | `Jumlah = 15`                                                                      | Berhasil |
| `02_jumlah_bilangan.py`     | `n = 10`                  | `Jumlah = 55`                             | `Jumlah = 55`                                                                      | Berhasil |
| `03_validasi_input.py`      | `120 → -5 → 75`           | 120 dan -5 ditolak, kemudian 75 diterima  | 120 ditolak, -5 ditolak, 75 diterima                                               | Berhasil |
| `04_hitung_genap.py`        | `n = 1`                   | `Banyak bilangan genap = 0`               | `Banyak bilangan genap = 0`                                                        | Berhasil |
| `04_hitung_genap.py`        | `n = 2`                   | `Banyak bilangan genap = 1`               | `Banyak bilangan genap = 1`                                                        | Berhasil |
| `04_hitung_genap.py`        | `n = 5`                   | `Banyak bilangan genap = 2`               | `Banyak bilangan genap = 2`                                                        | Berhasil |
| `04_hitung_genap.py`        | `n = 10`                  | `Banyak bilangan genap = 5`               | `Banyak bilangan genap = 5`                                                        | Berhasil |
| `kuis2_deret_aritmetika.py` | `a = 2, d = 3, n = 5`     | Suku: 2, 5, 8, 11, 14; jumlah = 40        | Suku: 2.00, 5.00, 8.00, 11.00, 14.00; jumlah = 40.00                               | Berhasil |
| `kuis2_deret_aritmetika.py` | `a = 10, d = -2, n = 4`   | Suku: 10, 8, 6, 4; jumlah = 28            | Suku: 10.00, 8.00, 6.00, 4.00; jumlah = 28.00                                      | Berhasil |
| `kuis2_deret_aritmetika.py` | `a = 1.5, d = 0.5, n = 3` | Suku: 1.5, 2.0, 2.5; jumlah = 6.0         | Suku: 1.50, 2.00, 2.50; jumlah = 6.00                                              | Berhasil |
| `kuis2_deret_aritmetika.py` | `n = 0`, lalu `n = 5`     | `n = 0` ditolak dan input diminta kembali | `n = 0` ditolak, kemudian program meminta `n` kembali dan berjalan setelah `n = 5` | Berhasil |

## Refleksi

Pada perulangan, batas iterasi dan perubahan variabel perlu diperhatikan agar program berhenti dan menghasilkan keluaran yang sesuai. Pada `for`, kesalahan dalam menentukan batas `range` dapat menyebabkan jumlah iterasi tidak sesuai. Pada `while`, variabel yang digunakan sebagai kontrol harus diperbarui agar kondisi dapat berubah menjadi `False` dan program tidak mengalami infinite loop.

Melalui latihan dan Kuis 2, saya memahami bahwa pemilihan `for` atau `while` disesuaikan dengan karakter masalah. `for` digunakan ketika jumlah iterasi telah diketahui, sedangkan `while` digunakan ketika perulangan bergantung pada suatu kondisi. Saya juga memahami penggunaan akumulasi untuk menyimpan hasil yang diperoleh secara berulang dan penggunaan seleksi `if` di dalam perulangan untuk memproses nilai berdasarkan kondisi tertentu.

Pada Kuis 2, saya menerapkan `while` untuk melakukan validasi terhadap nilai `n` dan `for` untuk menghasilkan suku deret sebanyak `n` kali. Pengujian beberapa test case membantu memastikan bahwa jumlah iterasi, nilai setiap suku, dan total deret telah sesuai dengan ketentuan.
