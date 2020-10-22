import math

def numbers(n:int):
    if(n<0):
        return

    print(n)
    numbers(n-1)

def fib(n:int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return fib(n-1) + fib(n-2)

def power(number: int, n: int) -> int:
    if n != 0:
        return number * power(number, n-1)
    else:
        return 1

def reverse(txt: str):
    if len(txt) == 0:
        return txt
    else:
        return reverse(txt[1:]) + txt[0]

def factorial(n: int) -> int:
    if n>=1:
        return n*factorial(n-1)
    else:
        return 1

def prime(n: int) -> bool:
    if n == 1:
        return False
    if n == 2:
        return True
    i = 1
    while (i*i < n):
        if(prime(i)):
            if (n % i == 0):
                return False
        i += 1
    return True

def n_sums(n: int):
    lista = []
    sumaParzystych = 0
    sumaNieparzystych = 0
    for liczba in range(int(math.pow(10,n-1)), int(math.pow(10,n))):
        liczba = str(liczba)
        for i in range(n):
            if i % 2 == 0:
                sumaParzystych += int(liczba[i])
            else:
                sumaNieparzystych += int(liczba[i])
        if sumaParzystych == sumaNieparzystych:
            lista.append(int(liczba))
            sumaNieparzystych = 0
            sumaParzystych = 0
    return lista
    
print(n_sums(2))


#numbers(20)                                     # Zadanie1
#print(f'Fib(10): {fib(10)}')                    # Zadanie2
#print(f'Power(2,10): {power(2,10)}')            # Zadanie3
#print(f'Reverse: {reverse("Odwrocony")}')       # Zadanie4
#print(f'Factorial(3): {factorial(3)}')          # Zadanie5
#print(f'Prime(11): {prime(11)}')                # Zadanie6