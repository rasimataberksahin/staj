import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from googletrans import Translator

# Google Translate çeviri işlemi için fonksiyon
def google_translate(text, target_language):
    translator = Translator()
    result = translator.translate(text, dest=target_language)
    return result.text

# Pencere oluşturma
pencere = tk.Tk()
pencere.title("Çok Dilli Çeviri Uygulaması")
pencere.geometry("600x400")

# Çeviri işlemini yapan fonksiyon
def cevir():
    en_cumle = tb1.get(1.0, tk.END).strip()  # Girilen metni al
    if not en_cumle:
        messagebox.showwarning("Uyarı", "Lütfen çevirilecek bir metin girin.")
        return
    
    # Seçilen diller
    from_lang = next((dil[1] for dil in diller if dil[0] == dil1.get()), "en")
    to_lang = next((dil[1] for dil in diller if dil[0] == dil2.get()), "tr")
    
    try:
        # Çeviriyi Google Translate API ile yap
        ceviri_cumle = google_translate(en_cumle, to_lang)
        tb2.delete(1.0, tk.END)
        tb2.insert(tk.END, ceviri_cumle)
    except Exception as e:
        messagebox.showerror("Hata", f"Çeviri sırasında bir hata oluştu: {e}")

# Temizleme işlemi yapan fonksiyon
def temizle():
    tb1.delete(1.0, tk.END)
    tb2.delete(1.0, tk.END)

# Etiketler
e1 = tk.Label(text="Çevrilecek Metin:", font="Arial 13 bold")
e1.place(x=10, y=10)
e2 = tk.Label(text="Çeviri Sonucu:", font="Arial 13 bold")
e2.place(x=10, y=160)

# Dil seçenekleri
diller = [("İngilizce", "en"), ("Türkçe", "tr"), ("Almanca", "de"), ("Fransızca", "fr"), ("İspanyolca", "es")]

# Dil seçim kutuları
tk.Label(text="Çıkış Dili:", font="Arial 11 bold").place(x=10, y=90)
tk.Label(text="Hedef Dili:", font="Arial 11 bold").place(x=300, y=90)

dil1 = ttk.Combobox(pencere, values=[dil[0] for dil in diller], state="readonly")
dil1.set("İngilizce")  # Varsayılan dil
dil1.place(x=100, y=90)

dil2 = ttk.Combobox(pencere, values=[dil[0] for dil in diller], state="readonly")
dil2.set("Türkçe")  # Varsayılan dil
dil2.place(x=390, y=90)

# Metin kutuları
tb1 = tk.Text(width=60, height=5)
tb1.place(x=10, y=40)
tb2 = tk.Text(width=60, height=5)
tb2.place(x=10, y=190)

# Butonlar
btn1 = tk.Button(text="ÇEVİR", font="Arial 13 bold", command=cevir)
btn1.place(x=100, y=320)
btn2 = tk.Button(text="TEMİZLE", font="Arial 13 bold", command=temizle)
btn2.place(x=300, y=320)

pencere.mainloop()
