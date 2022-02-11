def hesap(a,b,islem):
    if islem not in "+-*/":  #içinde yoksa
        return "lütfen geçerli değer gir"
    if islem=="+":
        return str(a) + " " + str(b) + " " + str(a+b)
    if islem == "-":
        return str(a) + " " + str(b) + " " + str(a+b) # diğer işlemleri yaz :D
    



while True: #devamlı dogruo oldugu sürece
    try :
        a = input("sayı git")
        b = input("sayı git")
        islem = input("işlem seç")
        print(hesap(a,b,islem))
    except:
        print("geçerli gir")


