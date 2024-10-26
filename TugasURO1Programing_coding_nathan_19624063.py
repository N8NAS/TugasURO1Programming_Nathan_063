
import random
def segitiga(a, t):
    i = 0
    choice = input("Ingin bikin segitiga jenis apa? \na) siku-siku dari kiri\nb) siku-siku dari kanan\nc) sama kaki\nd) sama kaki kebalik\n Jawab dengan huruf sesuai pilihan "
                   "(Alas segitiga untuk pilihan c dan d akan dua kali tinggi yang diinput serta kurang satu) : ")
    if choice.lower() == "a":
        q = a-1
        k = 1
        while i < t:
            print("* " * k + "_ "*q)
            k += 1
            i += 1
            q -= 1
    elif choice.lower() == "b":
        k = 1
        q = a - 1
        while i < t:

            print("_ "*q + "* "*k)
            i += 1
            q -= 1
            k += 1

    elif choice.lower() == "c":
        k = 1
        q = (a // 2) * 2 + 1
        if(a%2 == 0):
            print("Input angka ganjil untuk melaksanakan ini")
        else:
            while i < t:
                print("_ "*q + "* " * k + "_ "*q)
                q -= 1
                i += 1
                k += 2

    else:
        k = 2*a - 1
        if (a % 2 == 0):
            print("Input angka ganjil untuk melaksanakan ini")
        else:
            q = 0
            while i < t:
                print("_ "*q + "* "*k + "_ "*q)
                i += 1
                k -= 2
                q += 1
def persegi(s):
    i = 0
    while i < s:
        print("* "*s)
        i += 1
def persegi_panjang(p, l):
    i = 0
    while i < p :
        print("* "*l)
        i += 1


x = input("Mau membuat bentuk apa? \n a) Segitiga\n b) Persegi\n c) Persegi panjang\n d) Suprise me\n Jawab dengan huruf disebelah pilihan : ")
if x.lower() == "a":
    a = int(input("Berikan alas dan tinggi untuk segitiganya : "))
    segitiga(a, a)
elif x.lower() == "b":
    s = int(input("Berikan sisi untuk perseginya : "))
    persegi(s)
elif x.lower() == "c":
    p = int(input("Berikan panjang untuk persegi panjangnya : "))
    l = int(input("Berikan lebar untuk persegi panjangnya : "))
    persegi_panjang(p, l)
else :
    bebas = random.randint(1, 3)
    if bebas == 1 :
        a = random.randint(1, 100)
        segitiga(a, a)
    elif bebas == 2 :
        s = random.randint(1, 100)
        persegi(s)
    else:
        p = random.randint(1, 100)
        l = random.randint(1, 100)
        persegi_panjang(p, l)