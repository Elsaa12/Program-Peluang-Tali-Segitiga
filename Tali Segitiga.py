##Membuat Program Metode Tali 1 Meter

print("~"*50)
print("Program akan menampilkan Peluang terbentuknya segitiga dari pembagian \n\
        3 bagian acak dari tali 1 Meter")
print("~"*50)

from random import randint as toss
Lanjut = True

while Lanjut:
    win=0
    n=int(input("Masukan berapa kali anda ingin mencoba mengacak panjang tiap potongan: "))
    for i in range (1,n+1):
        tali1= toss(1,8)
        tali2= toss(1,10-tali1-1)
        tali3= int(10-tali1-tali2)
        
        print("tali A ",tali1/10,",Tali B ",tali2/10,",Tali C ",tali3/10)
        
        if tali1+tali2 <= tali3 or tali2+tali3 <= tali1 or tali1+tali3 <= tali2:
            print("tidak membentuk Segitiga")
        else :
            win+=1
            print("membentuk Segitiga")

    print(f"Peluang tali dapat membentuk segitiga dalam {n} kali percobaan adalah, {(win/n):.2}%")
    stop = input("Apakah anda ingin lanjut? \n input N jika ingin selesai : ")
    if stop.capitalize() == "N":
        Lanjut = False


