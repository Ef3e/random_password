import random
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import json

window = tk.Tk()

window.geometry("500x280+500+200")
window.title("password")
window.resizable(height=False,width=False)
window.configure(background="#DD4441")

uzunluk_label = tk.Label(window,text="sifre uzunlugu:",
                         font="bold 14",bg ="#DD4441",fg = "black" )

uzunluk_label.place(x=4,y=10)
uzunluklar = [u for u in range(8,33)]
uzunluklar_combo = ttk.Combobox(values=uzunluklar,width=11)
uzunluklar_combo.place(x=130,y=15)
sifre_goster = tk.Entry(window,fg="black",font="bold 10",width=30)
sifre_goster.place(x=5,y=50)
sifreler_kayit = tk.Listbox(window,bg="white",width=35,height=10,font="bold 10")
kaydir = ttk.Scrollbar(window,command=sifreler_kayit.yview)
kaydir.pack(side="right", fill="y")
sifreler_kayit.config(yscrollcommand=kaydir.set)
try:
    with open("sifreler.json","r",encoding="utf-8") as dosya:
        oku = json.load(dosya)
    for u in oku["sifreler"]:
        dize = "{}:\n{}".format(u["isim"],u["sifre"])
        sifreler_kayit.insert(tk.END,dize)
except:
    pass
sifreler_kayit.place(x=230,y=15)

def generate():
    sifre_goster.delete(0,tk.END)
    karakterler_liste = [] 
    karakterler = "1234567890asdfghjklwertyuiopzxcvbnmASDFGHJKLZXCVBNMQWERTYUIOP?.@*-\_+/"
    try:
        i = 0
        uzunluk = int(uzunluklar_combo.get())
        if uzunluk not in uzunluklar:
            messagebox.showerror("Hata","Lutfen gecerli bir deger girin")
        else:
            while i<uzunluk:
                karakter = random.choice(karakterler)
                karakterler_liste.append(karakter)
                i += 1
            sifre = "".join(karakterler_liste)
            karakterler_liste.clear()
            sifre_goster.insert(0,sifre)
    except:
        messagebox.showerror("Hata","Lutfen gecerli bir deger girin")
    
def kopyala():
    if len(sifre_goster.get()) < 8:
        messagebox.showerror("Hata","kapyalanabilecek sifre yok")
    else:
        window.clipboard_clear()
        window.clipboard_append(sifre_goster.get())  
        messagebox.showinfo("Basarili","Kopyalandi")

def veri_kaydet():
    if len(sifre_goster.get()) < 8:
        messagebox.showerror("Hata","kaydedilecek sifre yok")
    else:
        kayit = tk.Tk()

        kayit.geometry("280x160+925+200")
        kayit.title("*")
        kayit.resizable(width=False,height=False)
        kayit.configure(background="#ECEF25")

        isim_label = tk.Label(kayit,text="uygulama isimi:",bg="#ECEF25",fg="black",font="bold 12")
        isim_label.place(x=5,y=10)
        kayit_isim = tk.Entry(kayit,bg="white",fg="black",width=15,font="bold 10")
        kayit_isim.place(x=120,y=15)
        
        label_sifre = tk.Label(kayit,text="uygulama sifre:",bg="#ECEF25",fg="black",font="bold 12")
        label_sifre.place(x=5,y=60)
        kayit_sifre = tk.Entry(kayit,bg="white",fg="black",width=15,font="bold 10")
        kayit_sifre.insert(0,sifre_goster.get())
        kayit_sifre.place(x=120,y=62)
        
        def jsona_yazdir():
            al = {"isim":kayit_isim.get(),"sifre":kayit_sifre.get()}
            yaz = {"sifreler":[]}
            try:
                with open("sifreler.json","r",encoding="utf-8")as dosya:
                    oku = json.load(dosya)
                oku["sifreler"].append(al)
                with open("sifreler.json","w",encoding="utf-8") as dosya:
                    json.dump(oku,dosya,ensure_ascii=False,indent=4)
            except:
                yaz["sifreler"].append(al)
                with open("sifreler.json","w",encoding="utf-8") as dosya:
                    json.dump(yaz,dosya,ensure_ascii=False,indent=4)
            sifreler_kayit.delete("0",tk.END)
            with open("sifreler.json","r") as dd:
                okuyun = json.load(dd)
            for u in okuyun["sifreler"]:
                dize = "{}:\n{}".format(u["isim"],u["sifre"])
                sifreler_kayit.insert(tk.END,dize)
            kayit.destroy()
        yazdir = tk.Button(kayit,text="yazdir",command=jsona_yazdir,bg="white",fg="black",font="bold 12")
        yazdir.place(x=5,y=90)
        kayit.mainloop()


olustur = tk.Button(window,text="generate".upper(),font="bold 10",command=generate)
olustur.place(x=5,y=80)

kopya = tk.Button(window,text="kopyala".upper(),command=kopyala,font="bold 10")
kopya.place(x=147,y=80)

kaydet = tk.Button(window,width=8,height=1,text="kaydet".upper(),font="bold 10",command=veri_kaydet)
kaydet.place(x=80,y=120)
