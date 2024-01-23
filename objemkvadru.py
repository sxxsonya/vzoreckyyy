print("Vitejte v aplikaci pro vypocet objem kvadru")

#Deklarace (spise inicializace) promenych, nasledne do nich ukladame vstup
a = input("Zadejte promenou a:")
b = input("Zadejte promenou b:")
c = input("Zadejte promenou c:")

#pretypovani z stringu na integer
a = int(a)
b = int(b)
c = int(c)

#podminka, kontrola zda v promenych neni zaporne cislo 
if a>0 and b>0 and c>0:
    #Deklarace promene vysledek 
    vysledek = a*b*c
    #Output pro vysledek
    print("Vysledek je:", vysledek)
    #Pokud nebude platit prvni podminka, prvede se vzdy else
else:
    #Davame uzivateli vedet, ze neco zadal asi spatne
    print("tak jsi L?")

