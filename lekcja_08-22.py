
plik = open("symbole_przyklad.txt", 'r')
wiersze = plik.readlines()

# strip tylko na stringach

for i in range(len(wiersze)):
    wiersze[i] = wiersze[i].strip()

#for wiersz in wiersze:
#    wiersz = wiersz.strip() #tylko stripowany w forze

for wiersz in wiersze:
    czyPalindrom = True
    for i in range(6):
        if wiersz[i] != wiersz[11-i]:
            czyPalindrom = False
            break
    if czyPalindrom:
        print(wiersz)

for iWiersza in range(1, len(wiersze)): #od 1 wiersza do 19 - bo 20 zostanie pominięte
    for iZnaku in range(1, 12): #od 1 do 11 - bo 12 zostanie pominiete




