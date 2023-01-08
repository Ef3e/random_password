import random
print("şifreniz için enter tusuna basin")

while True:
    Sayi = "1234567890"
    kucuk = "asdfghjklwertyuiopzxcvbnm"
    buyuk = "ASDFGHJKLZXCVBNMQWERTYUIOP"
    simbol = "?.@*-\_+/"
    uzunluk = [8,9,10,11,12,13,14,15,16]
    soru = input("--"*15+"-")
    def sifre3():    
        sifre = Sayi + kucuk+buyuk+simbol
        uzunluk2 = random.choice(uzunluk)
        sifre2 = "".join(random.sample(sifre, uzunluk2))
        print(f"şifreniz = {sifre2}   --  uzunluk = {uzunluk2}")
    if soru == "" or soru =="e" :
        sifre3()
