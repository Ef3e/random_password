import random
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import json

sifre_pencere = tk.Tk()
sifre_pencere.geometry("200x90+500+200")
sifre_pencere.title("password")
sifre_pencere.resizable(height=False,width=False)
sifre_pencere.configure(background="#DD4441")
sifre_pencere.iconbitmap("iconum.ico")

sifre_olustur = tk.Entry(sifre_pencere,show="*",width=15,bg="white",fg="black",font="bold 12")
sifre_olustur.place(x=30,y = 25)

karakterler = "1234567890asdfghjklwertyuiopzxcvbnmASDFGHJKLZXCVBNMQWERTYUIOP?.@*-_+/"

def giris_yap():
    kontrol = False
    try:
        giris = open("JHY.txt","r")
        oku = giris.readline()
        sayi = 0
        for u in oku:
            if u in karakterler:
                sayi += 1 
                break
        if sayi == 0:
            giris = open("JHY.txt","w")
            giris.write(sifre_olustur.get())
            messagebox.showinfo("tamamlandi","sifre olusturuldu")
            sifre_olustur.delete(0,tk.END)
        if oku == sifre_olustur.get():
            kontrol = True
        else:
            sifre_olustur.delete(0,tk.END)
            messagebox.showerror("Hata","yanlis sifre girdiniz")
    except:
        giris = open("JHY.txt","w")
        giris.write(sifre_olustur.get())
        messagebox.showinfo("tamamlandi","sifre olusturuldu lutfen giris yapin")
        sifre_olustur.delete(0,tk.END)
        
    if kontrol:
        sifre_pencere.destroy()
        window = tk.Tk()
        window.geometry("500x320+500+200")
        window.title("password")
        window.resizable(height=False,width=False)
        window.configure(background="#DD4441")
        window.iconbitmap("iconum.ico")

        uzunluk_label = tk.Label(window,text="sifre uzunlugu:",
                                font="bold 14",bg ="#DD4441",fg = "black" )      
        ara = tk.Entry(bg="white",fg="black",font="bold 12",width=27)
        ara_bt = tk.Button(window,text="ARA",font="bold 10",fg="black")
        ara_bt.place(x=330,y=40)
        ara.place(x=230,y=15)
        uzunluk_label.place(x=4,y=10)
        uzunluklar = [u for u in range(8,33)]
        uzunluklar_combo = ttk.Combobox(values=uzunluklar,width=11)
        uzunluklar_combo.place(x=130,y=15)
        sifre_goster = tk.Entry(window,fg="black",font="bold 10",width=30)
        sifre_goster.place(x=5,y=50)
        sifreler_kayit = tk.Listbox(window,bg="white",width=35,height=14,font="bold 10")
        kaydir = ttk.Scrollbar(window,command=sifreler_kayit.yview)
        kaydir.pack(side="right", fill="y")
        sifreler_kayit.config(yscrollcommand=kaydir.set)
        
        try:
            with open("sifreler.json","r",encoding="utf-8") as dosya:
                oku = json.load(dosya)
            sifre = []
            for u in oku["sifreler"]:
                dize = "{}:{}".format(u["isim"],u["sifre"])
                sifre.append(dize)
            sifre.sort(reverse=False)
            for u in sifre:
                sifreler_kayit.insert(tk.END,u)
        except:
            pass
        sifreler_kayit.place(x=230,y=15)
        def generate():
            sifre_goster.delete(0,tk.END)
            karakterler_liste = []
            i = 0
            uzunluk = uzunluklar_combo.get()
            
            try:
                if uzunluk == "":
                    uzunluk = random.choice(uzunluklar)
                else:
                    uzunluk = int(uzunluk)
            except:
                messagebox.showerror("Hata","Gecerli bir deger girin") 
            if uzunluk not in uzunluklar: 
                messagebox.showerror("Hata","Gecerli bir deger girin") 
            else:
                while i<uzunluk:
                    karakter = random.choice(karakterler)
                    karakterler_liste.append(karakter)
                    i += 1
                sifre = "".join(karakterler_liste)
                karakterler_liste.clear()
                sifre_goster.insert(0,sifre)
            
        def kopyala():
            if len(sifre_goster.get()) < 8:
                messagebox.showerror("Hata","kopyalanacak oge bulunamadi")
            else:
                window.clipboard_clear()
                window.clipboard_append(sifre_goster.get())  
                messagebox.showinfo("Basarili","Kopyalandi")

        def veri_kaydet():

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
                if len(kayit_sifre.get()) < 8:
                    messagebox.showerror("Hata","sifre uzunlugu 8 den kisa 32 den uzun olamaz ")
                else:
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
                    with open("sifreler.json","r",encoding="utf-8") as dd:
                        oku = json.load(dd)
                    sifre = []
                    for u in oku["sifreler"]:
                        dize = "{}:{}".format(u["isim"],u["sifre"])
                        sifre.append(dize)
                    sifre.sort(reverse=False)
                    for u in sifre:
                        sifreler_kayit.insert(tk.END,u)
                    kayit.destroy()
            yazdir = tk.Button(kayit,text="kaydet",command=jsona_yazdir,bg="white",fg="black",font="bold 12")
            yazdir.place(x=5,y=90)
        def sec():
            girdi = sifreler_kayit.curselection() 
            # secilen nesneden baslayarak o nesneye kadar olan nesnellerin 
            # index numarasini verir
            if girdi:
                index = girdi[0] # ilk numara bizim secilen numaramizdir
                secilen = sifreler_kayit.get(index)
                return secilen  
        def sil_islem():
            try:
                with open("sifreler.json","r",encoding="utf-8") as dosya:
                    oku = json.load(dosya)
                secim = sec()
                secim = secim.split(":")
                for u in oku["sifreler"]:
                    if u["isim"] == secim[0] and u["sifre"] == secim[1]:
                        oku["sifreler"].remove(u)
                        break
                with open("sifreler.json","w",encoding="utf-8") as dosya:
                    json.dump(oku,dosya,ensure_ascii=False,indent=4)
                sifreler_kayit.delete(0,tk.END)
                sifre = []
                for u in oku["sifreler"]:
                    dize = "{}:{}".format(u["isim"],u["sifre"])
                    sifre.append(dize)
                sifre.sort(reverse=False)
                for u in sifre:
                    sifreler_kayit.insert(tk.END,u)
            except:
                messagebox.showerror("Hata","silinecek oge bulunamadi")
        
        def secileni_kopyala():
            try:
                sifre = sec()
                sifre = sifre.split(":")
                window.clipboard_clear()
                window.clipboard_append(sifre[1])  
                messagebox.showinfo("Basarili","Kopyalandi")
            except:
                messagebox.showerror("Hata","kopyalanacak oge bulunamadi")

        olustur = tk.Button(window,text="Generate".upper(),font="bold 10",command=generate)
        olustur.place(x=5,y=80)

        kopya = tk.Button(window,text="copy".upper(),width=8,command=kopyala,font="bold 10")
        kopya.place(x=147,y=80)

        kaydet = tk.Button(window,width=8,height=1,text="save".upper(),font="bold 10",command=veri_kaydet)
        kaydet.place(x=80,y=120)

        sil = tk.Button(window,text="delete".upper(),command=sil_islem,font="bold 10",width=10)
        sil.place(x=230,y=260)


        secilen_kopyala = tk.Button(window,text="copy password".upper(),command=secileni_kopyala,font="bold 10",width=15)
        secilen_kopyala.place(x=350,y=260)
        window.mainloop()
        
        
def goster():
    if sifre_olustur["show"] == "*": 
        sifre_olustur.config(show="") 
    else:
        sifre_olustur.config(show="*")

button = tk.Button(sifre_pencere,font="bold 10",command=goster,bg="white",fg="black",text="goster")
button.place(x=122,y=50)
label1 = tk.Label(text="SIFRENIZI YAZIN",bg="#DD4441",fg="black",font="bold 12").pack()
gir_buton = tk.Button(text="giris",fg="black",bg="white",command=giris_yap)
gir_buton.place(x=80,y=50)
sifre_pencere.mainloop()
