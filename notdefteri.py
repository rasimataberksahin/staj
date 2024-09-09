import tkinter as tk
from tkinter import filedialog  # Dosya açma ve kaydetme pencereleri için
#from tkinter import messagebox  # Hata mesajları için (bu örnekte kullanılmadı ama eklenebilir)

class TextEditor:
    def __init__(self, root):
        """Uygulamanın ana penceresi ve bileşenlerini başlatır."""
        self.root = root
        self.root.title("Metin Düzenleyici")  # Pencerenin başlığı
        self.root.geometry("600x400")  # Pencere boyutu (genişlik x yükseklik)
        
        # Menü çubuğunu oluşturur ve pencereye ekler
        self.menu = tk.Menu(root)
        root.config(menu=self.menu)
        
        # 'Dosya' menüsünü oluşturur ve 'menu'ye ekler
        self.file_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Dosya", menu=self.file_menu)
        
        # 'Dosya' menüsüne seçenekler ekler
        self.file_menu.add_command(label="Yeni", command=self.new_file)
        self.file_menu.add_command(label="Aç", command=self.open_file)
        self.file_menu.add_command(label="Kaydet", command=self.save_file)
        self.file_menu.add_command(label="Çıkış", command=root.quit)
        
        # Metin alanını oluşturur ve pencereye ekler
        self.text_area = tk.Text(root, wrap=tk.WORD)  # Metin kaydırma
        self.text_area.pack(expand=1, fill=tk.BOTH)  # Alanın genişlemesini ve pencereyi doldurmasını sağlar
        
    def new_file(self):
        """Yeni bir dosya oluşturur ve metin alanını temizler."""
        self.text_area.delete(1.0, tk.END)  # Metin alanındaki tüm içeriği siler
        self.root.title("Yeni Dosya - Metin Düzenleyici")  # Başlığı günceller
        
    def open_file(self):
        """Var olan bir dosyayı açar ve metin alanına yükler."""
        file_path = filedialog.askopenfilename(
            defaultextension=".txt",  # Varsayılan uzantı
            filetypes=[("Metin Dosyaları", "*.txt"), ("Tüm Dosyalar", "*.*")]  # Dosya türleri
        )
        if file_path:  # Dosya seçildiyse
            with open(file_path, 'r') as file:
                self.text_area.delete(1.0, tk.END)  # Önce mevcut içeriği siler
                self.text_area.insert(tk.END, file.read())  # Dosya içeriğini metin alanına ekler
            self.root.title(f"{file_path} - Metin Düzenleyici")  # Başlığı günceller
        
    def save_file(self):
        """Mevcut metni bir dosyaya kaydeder."""
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",  # Varsayılan uzantı
            filetypes=[("Metin Dosyaları", "*.txt"), ("Tüm Dosyalar", "*.*")]  # Dosya türleri
        )
        if file_path:  # Dosya yolu sağlandıysa
            with open(file_path, 'w') as file:
                file.write(self.text_area.get(1.0, tk.END))  # Metin alanındaki içeriği dosyaya yazar
            self.root.title(f"{file_path} - Metin Düzenleyici")  # Başlığı günceller

# Tkinter uygulamasını başlatır
if __name__ == "__main__":
    root = tk.Tk()  # Tkinter penceresini oluşturur
    app = TextEditor(root)  # Uygulamayı başlatır
    root.mainloop()  # Ana döngüyü başlatır, pencereyi açık tutar ve olayları işleyip yanıt verir
