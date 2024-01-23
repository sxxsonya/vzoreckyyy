print("Vitejte v aplikaci pro vypocet obsah kruhu")

#Deklarace (spise inicializace) promenych, nasledne do nich ukladame vstup
r = input("Zadejte promenou polomera r:")

#pretypovani z stringu na integer
r = int(r)

#podminka, kontrola zda v promenych neni zaporne cislo 
if r>0:
    #Deklarace promene vysledek 
    vysledek = 3.14*(r^2)
    #Output pro vysledek
    print("Vysledek je:", vysledek)
    #Pokud nebude platit prvni podminka, prvede se vzdy else
else:
    #Davame uzivateli vedet, ze neco zadal asi spatne
    print("tak jsi kokot?")

