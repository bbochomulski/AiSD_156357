def zad1(a,b):
    return a + "." + b

def zad2(a,b):
    a = a[0].capitalize()
    b = b.capitalize()
    return a + "." + b

def zad3(a,b,c):
    aktualny = int(str(a)+str(b))
    wiek = aktualny - c
    return wiek

def zad4(imie,nazwisko,foo):
    return foo(imie,nazwisko)

def zad5(dzielna, dzielnik):
    if dzielna>0 and dzielnik>0:
        return dzielna/dzielnik

def zad6():
    suma = 0
    while suma < 100:
        n = int(input("Podaj liczbe: "))
        suma += n
    print("Suma liczb: " + str(suma))

def zad7(lista):
    return tuple(lista)

def zad8():
    lista = []
    while len(lista) < 5:
        lista.append(int(input("Wprowadz wartosc: ")))
    return tuple(lista)

def zad9(liczba):
    tydzien = ['poniedzialek','wtorek','sroda','czwartek','piatek','sobota','niedziela']
    return tydzien[liczba-1]

def zad10(ciagZnakow):
    a = []
    b = []
    licznik = 0
    for znak in ciagZnakow:
        if licznik < int((len(ciagZnakow)/2)):
            a.append(znak)
        if licznik > int((len(ciagZnakow)/2)):
            b.append(znak)
        licznik += 1
    b.reverse()
    
    for i in range(int(len(a))):
        if a[i] != b[i]:
            print("Nie palindrom")
            return False
    print("To jest palindrom")
    return True

def zad10_prosta(ciagZnakow):
    rev = ''.join(reversed(ciagZnakow))

    if ciagZnakow != rev:
        print("Nie Palindrom")
        return False
    print("Palindrom")
    return True

print(zad1('B','Bochomulski'))
print(zad2('Bartosz','Bochomulski'))
print(zad3(20,20,1998))
print(zad4('Bartosz','Bochomulski',zad2))
print(zad5(4,3))
zad6()
lista = [3,3,7,9,3,4,6,8,9]
print(zad7(lista))
print(zad8())
print(zad9(4))
zad10('alsla')
zad11('allsa')