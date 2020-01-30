import file_manager

def lacz (a, b):
    c=[]
    for i in range(len(a)):
        if(i%2==0):
            c.append(a[i])
        else:
            c.append(b[i])
    return c

a=[1, 2, 3, 4, 5]
b=[5, 4, 3, 2, 1]
c=lacz(a,b)
print(c)


def data(data):
    print(dict([(" length ", len(data)), ('letters', list(data)), ('big_letters', data.upper()), ('small_letters', data.lower())]))

magic="KruCzeKu"
data(magic)

def trzy(text, letter):
    for char in letter:
        text = text.replace(char, "")
    print(text)

litera="uz"
trzy(magic, litera)

def temp(stop, type):
    if(type=='Fahrenheit'):
        print(stop*1.8+32)
    elif(type=='Rankine'):
        print((stop+273.15)*1.8)
    elif(type=='Kelvin'):
        print(stop+273.15)
    else:
        print("Bledny typ")



class Calculator:
    def add(self, a,b):
        print(a+b)


    def difference(self, s,b):
        print(a-b)


    def multiply(self, a,b):
        print(a*b)

    def divide(self, a, b):
        print(a/b)



class ScienceCalculator(Calculator):
    def potega(self, a, b):
        print(a^b)



def tyl(tekst):
    print(tekst[::-1])



plik = file_manager.FileManager("pliczek.txt")
print("Przed edycja:\n")
plik.read_file()
plik.update_file()
plik.zamknij()
krowa = file_manager.FileManager("pliczek.txt")
print("Po edycji:\n")
krowa.read_file()


