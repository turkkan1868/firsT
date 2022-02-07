
from ast import List
from operator import truediv
from traceback import print_tb


nmd = "dedemin torunu"


print(len(nmd))


## /yazi yaziyi alt satıra yazar
print(nmd[3]) # 0 1 2 3 


#sondan yaparken -1 le başlar 


# abcdefgh   [3:] defgh [:3] abc
# "ahmetyasi65"   [2:4] illk iki den başla 4 te dur == "me"

# [:::] kendisini yazar [::2 ] iki atlayarak  [1:10:3] bir de başla 10 da dur 3 er atlıyarak
#[::-1]  tersen yazar yazıyı 


ad = "halim klc"

print(ad.capitalize()) # il başı büyük yazar

print(ad)


# ad.split = ["halim",klc] ad.upper üyük yazar

benimListem= [10,20,30,40]
print(type(benimListem))


benimnumara = 10
digernumara = 20
listem = [benimnumara + digernumara]
listem[0] # 10 değerini verir



benimListem.append(50) #ekleme yapar


# benimListem.pop son elemanı çıkarır
# .remove(40) kırkı çıkartır
# .remove(ollmayan sayı) hata verir olmayan sayı diye
# .count(20) 20 den kaç tane var
# append ile aynı sayıyı bir daha ekleyebilirsin
listem2 = ["a","b"]
listem3 = ["sa","bs"]
toplam = listem2 + listem3 # ikisini yazar ["asd","asda"...]

toplam * 5 # 5 kere çarpar yazar

#bölmeye izin vermez

# .reverse tersen yazar


karisik ["a","b",2,3,4]

#type dersem list der karisik[0] type sorarsam int 
# nestedList = [1,2,"a",4,5[6,"z"]] type list verir
# Z almak için Zdegisken = nesteList[4] = [6,"z"] verir 
#nesteList[4][1] dersem o zaman "z" verir
# ilk dıştaki listeyi alırsın [1] sonra içindeki ikince [2] öyle öyle gider


#SÖZLÜK#
benimYemeklerim = ["elma","karpuz","muz"]
benimYemeklerim[1]#Karpuz
benimSozluk={"anahtarkelime":"deger"}
benimSozluk["anahtarkelime"]# deger yazar

benimYemekSozlugu = {"elma":100,"karpuaz" : 200} # SÖZLÜK {} İLE OLUR
benimYemekSozlugu["elma"]#100 yazar

benimYemekSozlugu["elma"] = 200 # yeni değer atar

digerSozluk= {150:"a",200 : "b"}
digerSozluk[150]#a yazar 200 de b yazar girilenin değeri gelir

digerSozluk.keys# ilk değerleri verir anahtar yani
digerSozluk.values# değerleri verir yani ikinciler

yeniSozluk={"anahtar1" : [2123,2,3,4,5], "anahtar2" : {"anahtar3" :5}}
yeniSozluk["anahtar1"][0] #listedeki 2123 getirir
yeniSozluk[anahtar2]["anahtar3"]# 5 getirir

#SEEEEEEEEEEETLERRRR#
#LİSTEDE AYNI ELEMANLAR OLABİLİR ama set karışır bir kere olur

benimListem1 = [1,2,3,5]
benimset= set(benimListem1)#type set verir # yazdırırsam aynıları bir sefer yazar


benimSetim = {"a","b","c"}#type set verir aynı harf iki ker olursa ikinciyi yazmaz
bosListe = [] # type list verir yazdırına [] verir
bosSet = {} #type yazarsan sözlük yazar !!!
BenimBosSetim = set () #type set yazar SETİ BÖYLE TANIMLAMALISIN !
BenimBosSozluk = dict() ##sözlük tanımlama
BenimBosSetim.add(5) #ekler

#TUPLE#
benimListem001= [1,2,"a",4.5] # [0] dersem 1 verir
benimListem001[0] = 100 #değer atar

benimTuple = (1,2,"a",4.5)
benimTuple[2] = "b" # hata verir diziden farkı dizide vermez .index ve count fonksiyonları var


#boolean#
#True false olayı
Benim = True
#type boool verir
10 > 5 #true verir 
listem = [500,666,663,333]
len(listem)#uzunlugu verir 4
sum(liste)# hepsini toplar 
ortalama = sum(listem)/len(listem)
listem[3]> ortalama #false verir ortalama yüksekse 
#######################
x=10
y=8
y>x #false verir 
3>1 or 3>2 #teki dogru olsa yeterli
3>1 and 3>2#ikisi de dogru olursa True verir İKİSİDE 
########################


#ifler#
if 3>1:
    print("dede") #dogruysa yazar
    
m = 4
k = 2

if m>k:
    print("")
elif k>x :
    print("")
else :
    print("")


benimKahraman = input("süuer kahraman seçiniz") #batman

if benimKahraman == "Batman" :
    print()
elif benimKahraman =="bebek" :
    print()
else :
    print()
    
    
    
a1 = 10 
b1 = 20
c1 = 30

if a1>b1 and b1>c1 : # or olsa ikisinden biri bunda ikiside çalışacak
    print()
elif a1 > b1 and b1 < c1:
    print()
    
    
candurumu = True

if candurumu  : #direk true olarak algılar truasa diye
    print()
else :
    print()

if not candurumu : # false mi diye yazar falseyse yazar
    print() 
    
    
    
bString = " halil  baba"
if bString == "halil baba" :
    print()
else :
    print() # true döndürür #her şeyi aynı olacak yoksa false döndürür
  
if "halil baba" in bString : #içinde var mı anlarız 
    print()
else:
    print()
    
bList = [10,29]

if 10 in bList :
    print()
else :
    print()  #true yazar
    
    
bSozluk = {"anahtar1":100}

if "anahtar10" in bSozluk.keys : # sözlükte varmı VAR .keys keyleri ilkleri listeler
    print()
else:
    print()
    
    
if 100 in bSozluk.values :
    print()#values ikincil değerler
else:
    print()
    
#DÖNGÜLER# #FOR#

b1liste=[10,20,30,40,50]

if 10 in b1liste :
    print()
    
for numara in b1liste:
    print(numara) #numaraya atar listedeki tek tek hepsini yazar
    
yoList=[3,4,5,6,7,2,13,5556,123]

for rakam in yoList:
    if rakam %2 == 0:
        print("çifttir")
      
      
        
# yeniListe="halil bey"
#for harf yeniListe:
#   print(harf) harfleri tek tek yaza

bnmTuple= (1,2,3,4,5)

for eleman in bnmTuple:
    print(eleman) # tek tek yazar -1 -2 -3 -4 şeklinde
    
koordinatList = [(10.2,15.2),(32.4,44.5)]
type(koordinatList)# List döndürür
type(koordinatList[0])#type dersem tuple döndürür

for j in koordinatList:
    print(j)# (10.2, 15.2) diğerlerini de bu şekil altına yazar
    print(eleman[0]) # 0.indeksi döndürür her parantezdeki yani 10.2 ve 32.4'ü
    #diğer bir yazdırma yöntemi altta

for (x,y) in koordinatList:
    print(x) # ilk indeksleri yazdırır 
    
b2Sozluk = {"anahtar1":100,"anahtar2":122}

for (anahtar,deger) in b2Sozluk:
    print(anahtar)#ilk değerleri yazdırır alt alta
    
    

yeniMist = [123,213231,55,55]

for mk1 in yeniMist:
    if mk1 == 15:
        break
    print(numara) # 15 e kdr yazar sonrasını yazmaz
    
    
for numara in yeniMist:
    if numara == 15:
        continue
    print(numara) #15 iyazmaz devam eder
    
for numara in yeniMist:
    pass # geç işlem yaapma

#while##

x1=0

while x1< 10:
    print(x1)
    print("hello")
    x1 = x1 + 1 # 10 a kadar yazar.
    

hList = [1,2,3,4,5]

hList.pop(5)
hList.append(5)
    
while 3 in hList:
    print("3 hala listede usTAAA")
    hList.pop() # sonelmanı çıkarır 3 çıkarınca durur

numara1 = 0
while numara < 5: # 0 1 2 3 yazar 4 e kdr
    if numara==4:
        break
    print(numara)
    numara = numara + 1
    
yeniDegi = 0
while yeniDegi < 15:
   # print("yeniDeg güncel değeri :" + str(yeniDegi)) alttaki diğer şekilde yazımı kolay
  # print(f"yeniDeg güncel değeri : {yeniDegi}") 
    #yeniDegi = yeniDegi + 1 #   ..... yeni degeri 1 ,2 ,3 ,4 diye yazar alt alta
 
 #METHOTLAR#
 
#list(range(25)) # 0 dan 25 e kdr liste oluştur  


for numara in list(range(15)):
    print(numara * 5) # 0 dan 15 e oluşturur ve 5 le çarpar
    
list(range(5,21,4)) # 5 den 4 er atlayarak 21 e kdr yazar 

index = 0
for numara in list(range(5,12)):
    print(f"güncel numara: {numara} güncel index {index}")
    
for eleman in enumerate(list(range(5,15))):
    print(eleman) #0,5 1,6 alt alt alta yaazar
    #index i kendi oluşturmuş oldu yukardaki gibi indexi elle vermedik
    #type yazırırsan tuple verir
    
for (index,numara) in enumerate(list(range(5,15))):
    print(index) # index 0 ddan başlayarak range den gelen sayılara index atar 0 burada indexleri yazzdırır
    print(numara) # numaraları yazdırır
    
from random import randint
randint(0,100) #0 dan yüze rastgele sayı döndürür

y1List = list(range(0,10))
y1List[randint(0,9)] #rastgele seçer benim yerime

from random import shuffle

shuffle(y1List) # karıştırır

#zip#
yemekList = ["muz","ananas"]
kaloriList = [100,200]
gunList =["pazartesi","salı","çarsamba"]

list(zip(yemekList,kaloriList,gunList)) # zip olarak verir o yuzden list yazıyorz
# list dediğimden list şekl yazar ("muz,100,"pazartesi") şeklnde hepsini 2 li grplar
ziplenmisListe = list(zip(yemekList,kaloriList,gunList)) # zip olarak verir o yuzden list yazıyorz

for eleman in ziplenmisListe:
    print(eleman)#y type tuple dir
    
listeOrnek = []
benimStr = " halil abep"

for harf in benimStr:
    listeOrnek.append(harf)

l1Ornek = " halil abep"
yOrnek = [eleman for eleman in l1Ornek] # tek tek alt alta "a" diye yazar
#forsuz direk yeni listenin içine atıyoruz 

ikinciOrnek= [numara * 5 for  numara in list(range(0,10))]
print(ikinciOrnek) # yeni 4 le çarpıklarını listeye ekler print eder


#FonksiyonlAR#

benimad= "halil baba"
benimad.upper() # fonksiyondur

def ilkfonk():
    print("ilk fonk")
    #çağırmadan çalışmaz mantıken
    
    
#input ve return


def merhaba(girdi):
    print("mrb baba")
    print(girdi)
    
merhaba("selam kız") # selam kız yazar :=)


def merhaba(isim = " selami"):
    print("merhaba") #direk çağırırssam merhaba sleami yazar değer verirsem selam (değer) yazar
    print(isim)
    
def toplama(n1,n2): # bu işlemlerde type sorarsam nonType der çünkü değer döndürmüyor !!!DDD
    print(n1+n2)
    
def donduren(n1,n2):
    return n1 + n2 #şimd type sorar san int der return vra çünk

def kontrolEt(s):
    if s == "halil" : #
        print()
    else:
        print()
        
#arg ve kwargs#
def yenitoplama(*args): # istediğin kadar girdi
    return sum(args)
yenitoplama(1231,131,23,123) # toplar verir 
#ytpe tuple 'dir

def ornekFonk(**kwargs):
    print(kwargs)
    
ornekFonk(muz = 100, elma = 200, meyve = 222) #dic şeklind yazar

def keyKontrol(**kwargs):
    if kwargs in "halil":
        print()
    else:
        print()
        
keyKontrol(halil = 100,zeynep=200) #True verir halil var ünkü

############33
def bolme(numara):
    return numara /2 

benimYyliste = [2,3,4,5,6,7,8,9]
yyListe = []

for eleman in benimYyliste:
   yyListe.append(bolme(eleman))
   #######################3
   
List(map(bolme,yyListe)) #ukardakinin kolay yapılışı 
#############################################

def kontrolEt(string):
    return "a" in string 

kontrolEt("atıl") #true döndürür
###############################################
# maple listeledğim listede sonuc.count(true) dersem map işlemini gerçekeltiği değerler sayısını döndürür
#list(filter(fonksiyonadı,hanglistedençekecek))
#filter da elemanları yazar map de true false diye değerlerini döndürür elemanların

#lambda#
carpma = lambda numara : numara *3
carpma(10)#30 yazar

list(map(lambda numara : numara *4,yyListe))
#map hepsine uygular

    

n1umara = 20
def carpma(rakam):
     n1umara=10
     return numara * numara
    
#20 yazar 

benimAd2 = " hakan"

def bKs():
    #enclosing
    benimAd2 = "halil"
    def icfonk():
        #local den dışarı dogru gidioyr varsa fonk en içindeki
        benimAd2="ayşe"
    icfonk()
    
    

    
    
 
 
    
    
      
    

    

    
    
    





