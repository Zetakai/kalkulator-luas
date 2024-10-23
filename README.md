# Kalkulator Luas Segitiga & Jajar Genjang

Program ini adalah aplikasi sederhana berbasis GUI (Graphical User Interface) yang menggunakan bahasa pemrograman Python dan pendekatan Pemrograman Berorientasi Objek (OOP) untuk menghitung luas segitiga atau jajar genjang. Pengguna dapat memilih bentuk yang diinginkan, memasukkan nilai alas dan tinggi, kemudian aplikasi akan menghitung dan menampilkan luas bentuk tersebut.

## Fitur
- Pengguna dapat memilih dua bentuk: **Segitiga** atau **Jajar Genjang**.
- Input alas dan tinggi dapat dimasukkan melalui antarmuka yang ramah pengguna.
- Hasil perhitungan luas ditampilkan dalam bentuk jendela pesan.
- Aplikasi ini menggunakan `Tkinter` untuk membuat antarmuka GUI.

## Instalasi

1. Pastikan Anda telah menginstal Python (versi 3 atau lebih baru) di komputer Anda. Jika belum, Anda bisa mengunduhnya di [python.org](https://www.python.org/downloads/).

2. Clone repositori ini atau salin file Python yang disertakan.

```bash
git clone https://github.com/Zetakai/kalkulator-luas.git
```
3. Masuk ke direktori proyek dan buat virtual environment (venv) menggunakan perintah:

```bash
cd kalkulator-luas
python -m venv env
```

4. Aktifkan virtual environment:

- Windows:
```bash
env/Scripts/Activate.ps1
```
- Linux/MacOS:
```bash
source env/bin/activate
```

5. Instal semua dependensi yang diperlukan dari file requirements.txt:

```bash
pip install -r requirements.txt
```
6. Jalankan program menggunakan Python:
   
```bash
python app.py
```

## Cara Penggunaan
1. Setelah program dijalankan, jendela GUI akan muncul dengan pilihan bentuk yang dapat dipilih: Segitiga atau Jajar Genjang.
2. Masukkan nilai alas dan tinggi pada kolom yang tersedia.
3. Klik tombol Hitung Luas untuk mendapatkan hasil perhitungan.
4. Hasil luas dari bentuk yang dipilih akan ditampilkan dalam jendela pop-up.

## Contoh
- Jika Anda memilih Segitiga dan memasukkan alas = 10 dan tinggi = 5, maka hasilnya adalah:
```plaintext
Luas segitiga adalah 25.00
```
- Jika Anda memilih Jajar Genjang dan memasukkan alas = 10 dan tinggi = 5, maka hasilnya adalah:
```plaintext
Luas jajar genjang adalah 50.00
```

## Persyaratan
- Python 3.x
- Modul Tkinter (sudah disertakan dalam instalasi Python standar)

## Struktur Proyek

```bash
kalkulator_luas/
│
├── app.py                # File utama yang berisi kode program
├── README.md             # Dokumentasi ini
├── requirements.txt      # Daftar dependensi yang diperlukan
├── env/                  # Virtual environment (tidak perlu diupload ke repositori)
```

## Menggunakan Virtual Environment (venv) dan requirements.txt
Aplikasi ini menggunakan virtual environment (venv) untuk mengisolasi dependensi dan paket Python serta file requirements.txt untuk mempermudah instalasi dependensi. Berikut adalah cara menggunakannya:

1. Buat virtual environment dengan perintah:

```bash
python -m venv env
```
2.  Aktifkan virtual environment:
- Windows:
```bash
env/Scripts/Activate.ps1
```
- Linux/MacOS:
```bash
source env/bin/activate
```
3.  Instal semua dependensi yang terdaftar di requirements.txt:
```bash
pip install -r requirements.txt
```
4.  Untuk menonaktifkan virtual environment, jalankan perintah:
```bash
deactivate
```

## Kontribusi
Jika Anda ingin berkontribusi dalam pengembangan aplikasi ini, Anda dipersilakan untuk membuat pull request atau mengirimkan issue.

## Lisensi
Proyek ini dilisensikan di bawah lisensi MIT. Silakan lihat file LICENSE untuk detailnya.

```markdown

### Penjelasan Tambahan:
1. **Instalasi dengan `requirements.txt`**: Langkah instalasi diperbarui untuk memasukkan penggunaan `requirements.txt` agar pengguna dapat menginstal semua dependensi sekaligus.
2. **Virtual Environment dan `requirements.txt`**: Bagian ini menjelaskan bagaimana mengisolasi proyek dan mengelola dependensi menggunakan virtual environment serta file `requirements.txt`.

Anda bisa menambahkan dependensi ke dalam file `requirements.txt` sesuai dengan kebutuhan proyek Anda.
```
