print("Vitejte v aplikaci pro vypocet obvodu obdelniku")

#Deklarace (spise inicializace) promenych, nasledne do nich ukladame vstup
a = input("Zadejte promenou a:")
b = input("Zadejte promenou b:")

#pretypovani z stringu na integer
a = int(a)
b = int(b)

#podminka, kontrola zda v promenych neni zaporne cislo 
if a>0 and b>0:
    #Deklarace promene vysledek 
    vysledek = 2*a+2*b
    #Output pro vysledek
    print("Vysledek je:", vysledek)
    #Pokud nebude platit prvni podminka, prvede se vzdy else
else:
    #Davame uzivateli vedet, ze neco zadal asi spatne
    print("tak jsi nadrbany?")

