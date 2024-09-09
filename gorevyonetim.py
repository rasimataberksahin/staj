import sqlite3  # Veritabanı işlemleri için
import tkinter as tk  # Tkinter arayüzü için
from tkinter import messagebox  # Tkinter'ın mesaj kutusu için

# Veritabanı işlemleri
def create_table():
    """Veritabanında görevler tablosunu oluşturur."""
    conn = sqlite3.connect('tasks.db')  #conn: Veritabanıyla etkileşimi sağlar
    cursor = conn.cursor()  #connect: SQL sorgularını çalıştırmak ve sonuçları işlemek için kullanılan bir nesnedir.
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            status TEXT CHECK(status IN ('pending', 'completed')) NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_task(title, description, status):
    """Yeni bir görev ekler."""
    conn = sqlite3.connect('tasks.db')  # Veritabanıyla etkileşimi sağlar.
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO tasks (title, description, status)
        VALUES (?, ?, ?)
    ''', (title, description, status))
    conn.commit()
    conn.close()

def update_task(task_id, title=None, description=None, status=None):
    """Mevcut bir görevi günceller."""
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    
    if title:
        cursor.execute('UPDATE tasks SET title = ? WHERE id = ?', (title, task_id))
    if description:
        cursor.execute('UPDATE tasks SET description = ? WHERE id = ?', (description, task_id))
    if status:
        cursor.execute('UPDATE tasks SET status = ? WHERE id = ?', (status, task_id))
    
    conn.commit()
    conn.close()

def delete_task(task_id):
    """Bir görevi siler."""
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()

def get_tasks():
    """Tüm görevleri listeler."""
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks')
    tasks = cursor.fetchall()
    conn.close()
    return tasks
#veritabanı kayıt işlemleri burada bitiyor.sırada tkinter arayüzü oluşturma var.

# Tkinter arayüzü
class TaskManagerApp:
    def __init__(self, root):#self:tanımladığım nesneler e erişmek için, root: ana pencereyi temsil ederler.
        self.root = root
        self.root.title("Görev Yöneticisi")
        self.root.configure(bg='darkblue')  # Ana pencerenin arka plan rengini lacivert yapma.
        self.root.geometry("500x300") # ana pencerenin büyüklüğünü girdiğim ibarelerde sabitleme.
        
        # Arayüz bileşenleri
        self.title_label = tk.Label(root, text="Başlık", bg="yellow")#başlık
        self.title_label.pack()

        self.title_entry = tk.Entry(root)#metin giriş alanı ekler
        self.title_entry.pack()

        self.description_label = tk.Label(root, text="Açıklama", bg="yellow")#açıklama
        self.description_label.pack()

        self.description_entry = tk.Entry(root)
        self.description_entry.pack()

        self.task_id_label = tk.Label(root, text="Görev ID",bg="yellow")#görev
        self.task_id_label.pack()
        
        self.task_id_entry = tk.Entry(root)
        self.task_id_entry.pack()

        self.status_label = tk.Label(root, text="Durum",bg="yellow")#durum
        self.status_label.pack()
        
        self.status_var = tk.StringVar(value="pending")#bekleyen görev butonu
        self.status_pending = tk.Radiobutton(root, text="Bekleyen", variable=self.status_var, value="pending")
        self.status_pending.pack()
        
        self.status_completed = tk.Radiobutton(root, text="Tamamlandı", variable=self.status_var, value="completed")#tamamlanan görev butonu
        self.status_completed.pack()

        self.add_button = tk.Button(root, text="Görev Ekle", command=self.add_task)#görev ekle tuşu
        self.add_button.pack()

        self.update_button = tk.Button(root, text="Görev Güncelle", command=self.update_task)#görev güncelle tuşu
        self.update_button.pack()

        self.delete_button = tk.Button(root, text="Görev Sil", command=self.delete_task)#görev sil tuşu
        self.delete_button.pack()

        self.show_button = tk.Button(root, text="Görevleri Göster", command=self.show_tasks)#görevleri göster tuşu
        self.show_button.pack()


#oluşturduğumuz arayüz bileşenlerine yapacaklarını ekleme kısmı
    def add_task(self):# görev ekleme kısmı
        title = self.title_entry.get()
        description = self.description_entry.get()
        status = self.status_var.get()
        if not title:
            messagebox.showerror("Hata", "Başlık girilmelidir!")
            return
        if len(title) < 3:
            messagebox.showerror("Hata", "Başlık en az 3 karakter uzunluğunda olmalıdır!")
            return
        if status not in ['pending', 'completed']:
            messagebox.showerror("Hata", "Geçersiz durum seçimi!")
            return
        add_task(title, description, status)
        messagebox.showinfo("Başarılı", "Görev eklendi!")
        self.clear_entries()

    def update_task(self):# görev güncelleme kısmı
        task_id = self.task_id_entry.get()
        if not task_id.isdigit():
            messagebox.showerror("Hata", "Geçersiz görev ID!")
            return
        task_id = int(task_id)
        title = self.title_entry.get()
        description = self.description_entry.get()
        status = self.status_var.get()
        if not title:
            messagebox.showerror("Hata", "Başlık girilmelidir!")
            return
        if len(title) < 3:
            messagebox.showerror("Hata", "Başlık en az 3 karakter uzunluğunda olmalıdır!")
            return
        if status not in ['pending', 'completed']:
            messagebox.showerror("Hata", "Geçersiz durum seçimi!")
            return
        update_task(task_id, title, description, status)
        messagebox.showinfo("Başarılı", "Görev güncellendi!")
        self.clear_entries()

    def delete_task(self):#görev silme kısmı
        task_id = self.task_id_entry.get()
        if not task_id.isdigit():
            messagebox.showerror("Hata", "Geçersiz görev ID!")
            return
        task_id = int(task_id)
        delete_task(task_id)
        messagebox.showinfo("Başarılı", "Görev silindi!")

    def show_tasks(self):#görev gösterme kısmı
        tasks = get_tasks()
        task_list = "\n".join([f"ID: {task[0]}, Başlık: {task[1]}, Açıklama: {task[2]}, Durum: {task[3]}" for task in tasks])
        messagebox.showinfo("Görevler", task_list)

    def clear_entries(self):#giriş kısmını temizleme kısmı
        """Giriş alanlarını temizler."""
        self.title_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)
        self.status_var.set("pending")
        self.task_id_entry.delete(0, tk.END)

# Veritabanını ve tabloyu oluştur
create_table()

# Tkinter uygulamasını başlat
root = tk.Tk()  # Tkinter ile pencereyi oluşturur ve temel pencereyi başlatır
app = TaskManagerApp(root)  # Ana pencereyi (root) parametre olarak alarak TaskManagerApp sınıfından bir uygulama örneği oluşturur ve kullanıcı arayüzünü başlatır
root.mainloop()  # Tkinter uygulamasının ana döngüsünü başlatır, böylece pencere açık kalır ve kullanıcı etkileşimlerini işleyebilir
