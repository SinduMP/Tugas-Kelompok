#Sistem Matematika
#Membuat Program Menghitung Luas dan keliling Bangun Datar 




from Ipython.display import clear_output

def cls() :
    clear_output(True)

pilihan = 1
while pilihan !=0:
    print("1. menghitung Luas bujur sangkar")
    print("2. menghitung Keliling bujur sangkar")
    print("3. menghitung Luas persegi panjang")
    print("4. menghitung Keliling persegi panjang")
    print("5. menghitung Luas segitiga")
    print("6. menghitung Keliling segitiga")
    print("7. menghitung Luas lingkaran")
    print("8. menghitung Keliling lingkaran")
    print("9. menghitung Luas jajar genjang")
    print("0. menghitung Keliling jajar genjang")
    
    pilihan = int(input("masukkan pilihan : "))
    print('')
    
    if pilihan == 1 :
        print("Luas bujur sangkar")
        print('')
        
