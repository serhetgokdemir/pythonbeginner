def tcNumCheck(tcnum):
    validTc = False
    if len(tcnum) != 11:
        print("Girilen TCKN 11 haneli değil.")
    elif tcnum[0]== "0" or int(tcnum[10])%2 != 0 :
        print("Geçersiz TCKN.")
    else:
        evens = sum(int(tcnum[i]) for i in range(0,9,2))
        odds = sum(int(tcnum[i]) for i in range(1,8,2))

        weirdsum = (evens*7-odds)%10
        toplam10 = (sum(int(tcnum[i]) for i in range(10)))%10

        if weirdsum != int(tcnum[9]): 
            print("Geçersiz TCKN.")
            print(evens,"\n",odds,"\n",weirdsum,"\n",toplam10)
        elif toplam10 != int(tcnum[10]):
            print("Geçersiz TCKN.")
        else:
            validTc = True
    
    return validTc




if __name__ == "__main__":
    validTc = False
    while not validTc:       
        tcnum = input("TCKN: ")
        validTc = tcNumCheck(tcnum)
        if validTc: print("Geçerli bir TC girdiniz.")

