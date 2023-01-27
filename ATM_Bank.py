print("**********GONULATM**********")
print("""
İşlemler:

1. Bakiye Sorgulama
2. Para Yatırma
3. Para Çekme
4. Hesaplarım arası para aktarımı
5. Çıkış

""")

Bakiye1 = 0
Bakiye2 = 0

while True:
    secim = input("Hangi İşlemi Yapmak İstiyorsunuz:")
    
    if secim == "1":
        print("BAKİYENİZ")
        print("Hesap 1 Bakiyeniz",Bakiye1,"TL")
        print("Hesap 2 BAkiyeniz",Bakiye2,"TL")
        
    elif secim == "2":
        print("BAKİYENİZ")
        print("Hesap 1 Bakiyeniz",Bakiye1,"TL")
        print("Hesap 2 Bakiyeniz",Bakiye2,"TL")
        hesap = input("Hangi Hesabınıza Para Yatıracaksınız 1/2 : ")
        miktar = float(input("Yatırmak İstediğiniz Miktar : "))
        
        if hesap == "1":
            Bakiye1 += miktar
        if hesap == "2":
            Bakiye2 += miktar
        print("_________")
        print("BAKİYENİZ")
        print("Hesap 1 Bakiyeniz",Bakiye1,"TL")
        print("Hesap 2 Bakiyeniz",Bakiye2,"TL")
        
    elif secim == "3":
        print("BAKİYENİZ")
        print("Hesap 1 Bakiyeniz",Bakiye1,"TL")
        print("Hesap 2 Bakiyeniz",Bakiye2,"TL")
        hesap = input("Hangi Hesabınızdan Para Çekeceksiniz 1/2 : ")
        miktar = float(input("Çekmek İstediğinz Miktar : "))
        
        if hesap == "1" and miktar <= Bakiye1 :
            Bakiye1 -= miktar
        elif hesap == "2" and miktar <= Bakiye2 :
            Bakiye2 -= miktar
        else:
            print("\n!!!YETERSİZ BAKİYE!")
        
        print("_________")
        print("BAKİYENİZ")
        print("Hesap 1 Bakiyeniz",Bakiye1,"TL")
        print("Hesap 2 Bakiyeniz",Bakiye2,"TL")
            
    elif secim == "4":
        print("BAKİYENİZ")
        print("Hesap 1 Bakiyeniz",Bakiye1,"TL")
        print("Hesap 2 Bakiyeniz",Bakiye2,"TL")
        hesap = input("Hangi Hesaba Para Aktaracaksınız 1/2 : ")
        miktar = float(input("Aktarmak İstedğiniz Miktar : "))
        
        if hesap == "1" and miktar != Bakiye1 :
            Bakiye1 += miktar
        else:
             Bakiye1 -= miktar
        if hesap == "2" and miktar != Bakiye2 :
            Bakiye2 += miktar
        else:
            Bakiye2 -= miktar
        
        print("_________")
        print("BAKİYENİZ")
        print("Hesap 1 Bakiyeniz",Bakiye1,"TL")
        print("Hesap 2 Bakiyeniz",Bakiye2,"TL")
        
    elif secim == "5":
        cıkıs = input("Çıkmak İstediğinizden eminmisiniz E/H : ")
        if cıkıs == "e" or cıkıs == "h" :
            print("...ÇIKIŞ İŞLEMİ YAPILDI...")
            break
        else:
            print("Geçersiz Tercih Yaptınız!!!")
            
    else:
        print("UYARI!!!\nGEÇERLİ BİR İŞLEM SEÇİNİZ")
        continue