#oppgave
#lag en liste fylt med 15 forskjellige tall som du velger selv.
#Legg deretter til et nytt tall på slutten av lista. Skriv ut listen
#Bytt det første elementet med nummer 3
#Fjern alle tall som er delelig med 3 fra listen. skriv ut listen til slutt

#løsning
#Jeg velger en liste som heter min_liste, jeg bruker range fra 1 til 16
#dvs at jeg får en liste fra 1 til 15, 16 er ikke med i listen.
#range gjør det lettere for meg, da tenger jeg ikke å skrive hvert tall
min_liste=list(range(1,16))
#jeg skriver ut listen ved å bruke print
print(min_liste)
#når jeg skriver liste navn dot append, det hjelper å skrive tallet jeg velger
#i slutten av listen
min_liste.append(17)
#jeg skriver ut listen ved å bruke print
print(min_liste)
#her bytter jeg ut det første elementet med 3
min_liste[0]= 3
#jeg skriver ut listen ved å bruke print
print(min_liste)
#her bruker jeg for loops for å skjekke hvert tall i listen
#jeg bruker if-testen,hvis tallet gir null i resten, er det delelig med tre
#jeg bruker remove for å fjerne hvert element som er delelig med 3
#jeg skriver ut listen til slutt
for elem in min_liste:
    if elem % 3 == 0:
        min_liste.remove(elem)
print(min_liste)
