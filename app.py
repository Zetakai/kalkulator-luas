import tkinter as tk
from tkinter import messagebox

# Kelas dasar untuk bangun datar
class BangunDatar:
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi

# Kelas Segitiga yang mewarisi dari BangunDatar
class Segitiga(BangunDatar):
    def hitung_luas(self):
        return 0.5 * self.alas * self.tinggi

# Kelas Jajar Genjang yang mewarisi dari BangunDatar
class JajarGenjang(BangunDatar):
    def hitung_luas(self):
        return self.alas * self.tinggi

# Kelas GUI
class KalkulatorLuasGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Kalkulator Luas")

        # Membuat label, entry, dan tombol
        self.label_bangun = tk.Label(root, text="Pilih Bangun Datar:")
        self.label_bangun.pack()

        self.pilihan_bangun = tk.StringVar(value="Segitiga")
        self.radio_segitiga = tk.Radiobutton(root, text="Segitiga", variable=self.pilihan_bangun, value="Segitiga")
        self.radio_segitiga.pack()
        self.radio_jajargenjang = tk.Radiobutton(root, text="Jajar Genjang", variable=self.pilihan_bangun, value="Jajar Genjang")
        self.radio_jajargenjang.pack()

        self.label_alas = tk.Label(root, text="Alas:")
        self.label_alas.pack()

        self.entry_alas = tk.Entry(root)
        self.entry_alas.pack()

        self.label_tinggi = tk.Label(root, text="Tinggi:")
        self.label_tinggi.pack()

        self.entry_tinggi = tk.Entry(root)
        self.entry_tinggi.pack()

        self.tombol_hitung = tk.Button(root, text="Hitung Luas", command=self.hitung_luas)
        self.tombol_hitung.pack()

    def hitung_luas(self):
        try:
            alas = float(self.entry_alas.get())
            tinggi = float(self.entry_tinggi.get())

            if self.pilihan_bangun.get() == "Segitiga":
                bangun = Segitiga(alas, tinggi)
            else:
                bangun = JajarGenjang(alas, tinggi)

            luas = bangun.hitung_luas()
            messagebox.showinfo("Hasil", f"Luas {self.pilihan_bangun.get().lower()} adalah {luas:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Masukkan angka yang valid untuk alas dan tinggi")

# Program utama
if __name__ == "__main__":
    root = tk.Tk()
    app = KalkulatorLuasGUI(root)
    root.mainloop()
