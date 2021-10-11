#her velger jeg liste med tre forskjellige tall
min_liste = [19, 1, 2000]
#jeg bruker append for å legge til tallet 2020 i slutten av listen
min_liste.append(2020)
#jeg skriver ut listen
print(min_liste)
#her ville jeg skjekke om 2020 er i listen, det gir True, dvs det er i listen
print((2020) in min_liste)
#her skriver jeg ut det første elementet og det tredje ved bruk av indeksen
print("Det første elementet er", min_liste[0], "Og det tredje er", min_liste[2])
#jeg bruker en ny liste som ber brukeren om å gi meg fire forskjellige navn
bruker_liste = []
navn1= input("gi meg ett navn! ")
#jeg bruker lower for å sikre at jeg får lite bokstaver
navn1=navn1.lower()
navn2= input("gi meg et annet navn! ")
navn2=navn2.lower()
navn3= input("gi meg et navn til! ")
navn3=navn3.lower()
navn4= input("gi meg det siste navnet! ")
navn4=navn4.lower()
#jeg lager listen ved bruk av de fire navn variablene
bruker_liste= [navn1, navn2, navn3, navn4]
#jeg skriver ut listen
print(bruker_liste)
#jeg bruker if testen for å teste om brukeren har skrevet navnet mitt
if "rawan" in bruker_liste:
#hvis brukeren har skrevet navnet mitt skulle det printe du husket meg
    print("Du husket meg!")
#hvis brukeren ikke har gjort det, skulle det printe glemte du meg
else:
    print("Glemte du meg?")
#her regner jeg summer av lista mi ved å addere sammen alle indekser
sum= (min_liste[0])+(min_liste[1])+(min_liste[2])+(min_liste[3])
#jeg skriver ut summen
print(sum)
#her regner jeg produktet av lista mi ved å multiplisere  alle indekser
produkt= (min_liste[0])*(min_liste[1])*(min_liste[2])*(min_liste[3])
#jeg skriver ut produktet
print(produkt)
#jeg lager en ny lista som inneholder sum og produkt
ny_liste=[sum, produkt]
#jeg skriver ut listen
print(ny_liste)
#her bruker jeg en liste til for å slå sammen de to listene fra før
mer_liste= min_liste+ny_liste
#jeg skriver ut listen
print(mer_liste)
#her ville jeg fjerne de to siste elementene fra lista ved bruk av del (delete)
#ved å skrive 4:6 betyr det fra indeks fire til indeks 5, indeks 6 er ikke med
del mer_liste[4:6]
#jeg skirver ut lista til slutt 
print(mer_liste)
