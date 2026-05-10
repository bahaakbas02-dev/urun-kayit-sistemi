import tkinter as tk
from tkinter import messagebox

def sayfa_degistir(frame):
    frame.tkraise()

root = tk.Tk()
root.title("Ürün Paneli")
root.geometry("600x700")

sayfa1 = tk.Frame(root)
sayfa2 = tk.Frame(root)


for sayfa in (sayfa1, sayfa2):
    sayfa.grid(row=0, column=0, sticky='news')

urunler = []

# Sayfa 1: Ürün Listesi
tk.Label(sayfa1, text="Mevcut Ürünler", font=("Arial", 16, "bold")).pack(pady=10, padx=200)

liste_kutusu = tk.Listbox(sayfa1, font=("Arial", 12))
liste_kutusu.pack(pady=10)

def urun_sil():
    try:
        secili = liste_kutusu.curselection()[0]
        silinen_urun = liste_kutusu.get(secili)
        urunler.remove(silinen_urun)
        liste_kutusu.delete(secili)
    except:
        messagebox.showwarning("Uyarı", "Lütfen silmek için bir öğe seçin")

def listeye_ekle():
    liste_kutusu.delete(0, tk.END)
    for urun in urunler:
        liste_kutusu.insert(tk.END, urun)         

listeye_ekle()


tk.Button(sayfa1, text="Ürün Sil", command=urun_sil, bg="#FF0000").pack(pady=10)
tk.Button(sayfa1, text="Ürün Ekle ->", command=lambda: sayfa_degistir(sayfa2), bg="#0080FF").pack(pady=20)

# Sayfa 2: Ürün Girişi

tk.Label(sayfa2, text="Ürün Ekle", font=("Arial", 16, "bold")).pack(pady=10, padx=200)
tk.Label(sayfa2, text="Ürün Adı: ").pack()
giris_alani = tk.Entry(sayfa2, font=("Arial", 12))
giris_alani.pack(pady=5)

def urun_kaydet():
    yeni_urun = giris_alani.get()
    if yeni_urun:
        urunler.append(yeni_urun)
        listeye_ekle()
        giris_alani.delete(0, tk.END)
        sayfa_degistir(sayfa1)

tk.Button(sayfa2, text="Kaydet", command=urun_kaydet, bg="#00ff22").pack(pady=10)
tk.Button(sayfa2, text="<- Geri Dön", command=lambda: sayfa_degistir(sayfa1), bg="#ff0000").pack(pady=5)

sayfa_degistir(sayfa1)

root.mainloop()
