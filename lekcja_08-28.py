
import math

plik = open("przyklad.txt", 'r')
wiersze = plik.readlines()

numbers = []
napisy = []

for i in range(len(wiersze)):
    wiersze[i] = wiersze[i].strip()
    numbers.append(int(wiersze[i][:2])) #int(jakis string liczbowy) - zamieni stringa na liczbe
    indeks_spacji = wiersze[i].find(" ")+1 #znajdujemy pozycje spacji
    napisy.append(wiersze[i][indeks_spacji:])

#PODPUNKT 1
#36: 1, 2, 3, 4, 6, 9, 12, 18, 36

#potega: liczba ** 2 - potęga 2
#pierwiastek: liczba ** 0.5 - potęga 0.5 - pierwiastek 2 stopnia

#string - ciag znakow - czyli np. "HELLO"
#float - przecinkowa

#sito erastotenesa
pierwsze = [True] * 101
pierwsze[0] = pierwsze[1] = False
for i in range(2, 101):
    if (pierwsze[i]): #
        for j in range(i*i, 101, i):  #trzeci argument w range to jest o ile zwiększamy
            pierwsze[j] = False

#jak działa?
#dla i = 2, pętla j będzie przyjmowac jej wielokrotnosci: 4, 6, 8, 10, 12, 14, 16, ...
#dla i = 3, pętla j będzie przyjmować wielokrotnosci 3: 9, 12, 15, 18, 21, ...

#liczba = 24
#2+22, 3+21, 4+20, ..., 22+2
# 6 = 3+3

for liczba in numbers:
    if (liczba % 2 == 0):
        for j in range(2, int(liczba/2)+1):
            if (pierwsze[j] and pierwsze[liczba-j]):
                print(str(liczba) + " " + str(j) + " " + str(liczba-j))
                break #konczy najbliższą petle

#PODPUNKT 2
for napis in napisy:
    # baaaaac
    obecna_dlugosc = 1
    obecny_poczatek = 0
    max_dlugosc = 1
    max_poczatek = 0
    for i in range(1, len(napis)):
        if (napis[i] == napis[i-1]):
            obecna_dlugosc += 1
        else:
            obecna_dlugosc = 1
            obecny_poczatek = i
        if (obecna_dlugosc > max_dlugosc):
            max_dlugosc = obecna_dlugosc
            max_poczatek = obecny_poczatek
    print(napis[max_poczatek:(max_poczatek+max_dlugosc)] + " " + str(max_dlugosc))


