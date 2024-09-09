"""from tkinter import *
pencere=Tk()
pencere.title("Hesap Makninesi")
pencere.geometry("270x250+300+100")
pencere.resizable(FALSE,FALSE)

depo=""

ekran=Entry(width=40, justify=RIGHT)
ekran.grid(row=0,column=0,columnspan=3,ipady=4)

liste = ["1","2","3","4","5","6","7","8","9","0","+","-","/","*","=","C"]

sira=1
sutun=0

for i in liste:
    komut = lambda x=i: hesapla(x)#i nin alacsağı ilk değer 1.Ben bu 1 değerini x e atıyorum ve hesaplama kısmına bu 1 değerini gönderiyorum.
    Button(text=i,font="verdana 8 bold",width=10,height=2,relief=GROOVE,command=komut).grid(row=sira,column=sutun)
    sutun+=1#her seferinde bir arttırmamın sebebi: butonların üst üste gelmesini istemiyoruz.
    sutun+=1
    if sutun>2:
        sutun=0#bir alt satıra geçtiğinde ilk buton sıfırıncı sütunda olmalı
        sira +=1#bir alt satıra geçmesi için sıranın da her seferinde bir artması gerekiyor.

mainloop()       """ 


"""
from tkinter import *
import math

pencere = Tk()
pencere.title("FENERBAHÇE")
pencere.geometry("270x250+300+100")
pencere.resizable(FALSE, FALSE)
pencere.config(bg="#333333")

depo = ""

def hesapla(tus):
    global depo
    if tus in "0123456789":
        ekran.insert(END,tus)
        depo = depo + tus

    if tus in "+-/*":  
        ekran.insert(END,tus)
        depo = depo + tus

    if tus == "=":
        ekran.delete(0,END)
        hesap = eval(depo, {"__builtins__",None},{})    
        depo = str(hesap)
        ekran.insert(END,depo)

    if tus == "C":
        ekran.delete(0,END)
        depo=""


ekran = Entry(width=40, justify=RIGHT)
ekran.grid(row=0, column=0, columnspan=3, ipady=4)

liste = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "+", "-", "/", "*", "=", "C"]

sira = 1
sutun = 0

for i in liste:
    komut = lambda x=i: hesapla(x)  # i'nin alacağı ilk değer 1. Ben bu 1 değerini x'e atıyorum ve hesaplama kısmına bu 1 değerini gönderiyorum.
    Button (text=i, font="verdana 8 bold",bg="#828282", width=10, height=2, relief=RAISED, command=komut).grid(row=sira, column=sutun)
    sutun += 1  # her seferinde bir arttırmamızın sebebi: butonların üst üste gelmesini istemiyoruz.
    if sutun > 2:
         sutun = 0  # bir alt satıra geçtiğinde ilk buton sıfırıncı sütunda olmalı
         sira += 1  # bir alt satıra geçmesi için sıranın da her seferinde bir artması gerekiyor.

mainloop() 

"""

###EN GÜZEL ÇALIŞAN###

from tkinter import *

pencere = Tk()
pencere.title("FENERBAHÇE")
pencere.geometry("270x250+300+100")
pencere.resizable(FALSE, FALSE)
pencere.config(bg="#333333")

depo = ""

def hesapla(tus):
    global depo
    if tus in "0123456789":
        ekran.insert(END, tus)
        depo += tus
    elif tus in "+-/*":  
        ekran.insert(END, tus)
        depo += tus
    elif tus == "=":
        try:
            hesap = str(eval(depo))  # Güvenlik açısından basit bir eval kullanımı
            ekran.delete(0, END)
            ekran.insert(END, hesap)
            depo = hesap  # Sonucu depoya kaydediyoruz, böylece yeni işlemler bu sonuçla devam eder
        except Exception as e:
            ekran.delete(0, END)
            ekran.insert(END, "Hata")
            depo = ""
    elif tus == "C":
        ekran.delete(0, END)
        depo = ""

ekran = Entry(pencere, width=40, justify=RIGHT)
ekran.grid(row=0, column=0, columnspan=3, ipady=4)

liste = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "+", "-", "/", "*", "=", "C"]

sira = 1
sutun = 0

for i in liste:
    komut = lambda x=i: hesapla(x)
    Button(pencere, text=i, font="verdana 8 bold", bg="#828282", width=10, height=2, relief=RAISED, command=komut).grid(row=sira, column=sutun)
    sutun += 1
    if sutun > 2:
        sutun = 0
        sira += 1

mainloop()
