# Basit hesap makinesi

def calculator():
    Sayi = 0
    print(Sayi)
    while True:
        opr = input("Operatörü giriniz: ")

        if opr == "C": Sayi = 0
        else: 
            Sayi2 = int(input("Sayı:"))
            if opr == "+": Sayi+=Sayi2
            elif opr == "-": Sayi-=Sayi2
            elif opr == "*": Sayi*=Sayi2
            elif opr == "/": Sayi/=Sayi2
            else: print("Geçersiz operatör girdiniz.")

        print(Sayi)


if __name__ == "__main__":
    print("---------Basit hesap makinesi programı---------")
    print("Geçerli operatörler: '+'  '-'  '*'  '/'")
    print("Sıfırlamak için 'C' yazınız.")
    calculator()