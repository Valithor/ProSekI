c= 'Lorem Ipsum jest tekstem stosowanym jako przykładowy\n' \
   'wypełniacz w przemyśle poligraficznym. Został po raz pierwszy \n' \
   'użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem \n' \
   'próbnej książki. Pięć wieków później zaczął być używany przemyśle \n' \
   'elektronicznym, pozostając praktycznie niezmienionym. \n' \
   'Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy \n' \
   'Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z \n' \
   'zawierającym różne wersje Lorem Ipsum oprogramowaniem \n' \
   'przeznaczonym do realizacji druków na komputerach osobistych, \n' \
   'jak Aldus PageMaker. \n'

def szukaj(litera, tekst):
    liczba_liter=0
    for i in range(len(tekst)):
        if litera==tekst[i]:
            liczba_liter = liczba_liter +1
    return liczba_liter


def wyswietl(el):
    for key, value in el.items() :
        print (str(key) + " to " +  str(value))

imie = 'Milosz'
nazwisko = 'Miotk'
litera_1 = imie[1]
litera_2 = nazwisko[2]
liczba_liter1 = szukaj(litera_1, c)
liczba_liter2 = szukaj(litera_2, c)
print(liczba_liter2)
print('W tekście jest '+ str(liczba_liter1) + ' liter ' + litera_1 + ' oraz ' + str(liczba_liter2) + ' liter ' +litera_2)

napis = 'ala'
## print(dir(napis))
## help(napis.isspace())

print(imie[::-1])
print(nazwisko[::-1])

def split(lista):
    half = len(lista)//2
    return lista[:half], lista[half:]

lista = [1,2,3,4,5,6,7,8,9,10]
print(lista)
lista, lista2 = split(lista)
print(lista, lista2)
lista=lista + lista2
lista.insert(0,0)
print(lista)

krz = ["Krzys Winiary", 10293]
an= ["Änia Niedowiary", 32131]
ja= ["Jacek Krzyzanowski", 23131]
studenci = krz, an, ja
print(studenci)

slownik= dict([(10293, krz + [21, "krzys@wp.pl", 1992, "Sloneczna 12"]), (32131, an + [18, "ania@wp.pl", 1995, "Prosper 2"]), (23131, ja +[22, "jacus@wp.pl", 1991, "Karpia 12"])])
print(slownik.values())

tel = [3213, 6725, 8962, 3213, 8962]
print(tel)
tel=list(set(tel))
print(tel)

for i in range(1, 11):
    print(i, end=', ')
print("\n")
for i in range(100, 19, -5):
    print(i, end=', ')
print("\n")


sl1= dict([(1,"jeden"), (2,'dwa'), (3,'trzy')])
sl2= dict([(1,"cztery"), (2,'piec'), (3, 'szesc')])
sl3= dict([(1,"siedem"), (2,'osiem'), (3,'dziewiec')])
superlista=[sl1, sl2, sl3]
print(sl1[1])
for i in range(len(superlista)+1):
    print("Slownik "+str(i))
    if(i==1):
        wyswietl(sl1)
    elif(i==2):
        wyswietl(sl2)
    elif(i==3):
        wyswietl(sl3)
