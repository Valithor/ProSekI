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