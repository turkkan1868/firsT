benimList  = list()
type(benimList)#list verir


class superman():
    
    
    def __init__(self,isim,yas,meslek):
        self.isim = isim
        self.yas = yas
        self.meslek = meslek
        print("çağrıldı")
    def ornekMethod(self):#selfy yazmazsan print etmez
        print(f"özel kahramanım meslegim {self.meslek}") #self sınıftan çeker yoksa bulamaz mesleği
supern =superman() #printi yazar #3 girdiyi yazacan yoksa hata verir
supern#. içindekiler çıkar isim yas meslek vvb

supern.ornekMethod # paraentez koymazsan print etmez



class kopek():
    yilCarpanı = 7
    def __init__(self,yas=5): # 5 değeri default değer verilmezse yazar
        self.yas = yas
         
    def insanyasihesap(self):
        return self.yas #* #Kopek.yilCarpanı
benimkope = kopek(3) # benimkope.yas çağırınca 3 yazar


#İNHERTİNCE MİRAS #


class Hayvan():
    def __init__(self):
        print()
        
    def methot1(self):
        print()
        
        
benimhayvan = Hayvan()
benimhayvan.methot1()


class Kedi(Hayvan):
    def __init__(self):
        hayvan.__init__(self)
        print()
    def methot1(self):
        print() #override 
        
benimKedi = Kedi()

benimKedi.methot1() #miras aldı 





class Meyve(0):
    def __init__(self,isim,kalori):
        self.kalori = kalori
    def __str__(self):
        return f"{self.isim} şu kadar kalori {self.kalori}"
    def ___len__(self):
        return self.kalori
        
muz = Meyve("muz",150)
muz.kalori # 150 yazar
#muz yazdırmaya çalışırsan print etmez hafıza yeri yazar
BenimListt = [1,2,3,4,"a"]
print(BenimListt) # listeyi yazaar
#muzun len yazsam yazmaz çünkü özel def açıp str ve len yazmam lazım

        
        
import numpy
import matplotlib.pyplot


