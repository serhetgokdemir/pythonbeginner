# Basit hesap makinesi

def calculator():
    Sayi = 0
    print(Sayi)
    while True:
        opr = input("Operatörü giriniz: ")

        if opr == "Q":
            print("Hesap makinesi programından çıkılıyor...")
            break
        if opr == "C": Sayi = 0
        else: 
            try:
                Sayi2 = int(input("Sayı:"))
                if opr == "+": Sayi+=Sayi2
                elif opr == "-": Sayi-=Sayi2
                elif opr == "*": Sayi*=Sayi2
                elif opr == "/": 
                    try: Sayi/=Sayi2
                    except ZeroDivisionError:
                        print("Sayı 0'a bölünemez.")    
                else: print("Geçersiz operatör girdiniz.")
            except ValueError:
                print("Geçerli bir sayı giriniz.")

        print(Sayi)


if __name__ == "__main__":
    print("---------Basit hesap makinesi programı---------")
    print("Geçerli operatörler: '+'  '-'  '*'  '/'")
    print("Sıfırlamak için 'C' yazınız.")
    print("Çıkış Yapmak için 'Q' yazınız.")
    calculator()