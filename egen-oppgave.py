#Tenk deg at du er en matte lærer, du skal lage en quiz for elevene dine.
#Skriv et program som ber eleven om å svare på 2 spørsmål knyttet til matte.
#Du må du be eleven om å skrive navnet sitt.
#Første spørsmål skal være "hva er log10". Lagre svaret i en variabel.
#Skriv en if-sjekk som tester hva brukeren har skrevet inn:
#a. Hvis eleven har svart “1” skal programmet skrive ut “riktig svar"
#b. Hvis eleven har svart noe helt annet skal programmet skrive ut “feil svar"
#Andre spørsmål skal være "gi meg et tall som er mindre enn 100 og delelig med 2"
#a. Hvis eleven har gitt et tall som er mindre enn 100 og delelig med 2
#skriv ut "riktig svar"
#b. Hvis eleven har gitt et tall som er større enn 100 mens delelig med 2
#skriv ut "Feil svar, det er delelig med 2 men større enn 100"
#c. Hvis eleven har svart noe helt annet, skriv ut "feil svar"
#til slutt, hvis eleven har svart riktig på begge spørsmålene
#skriv ut ("Bra", navn,  "du fikk alt riktig")
navn= input("Hva heter du? ")
navn= navn.lower()
print("Hei", navn , "Velkommen til matte quiz")
sporsmaal1= int(input("Hva er log10? "))
if sporsmaal1 == 1:
    print("Bra", navn, "riktig svar")
else:
    print("Feil svar")
sporsmaal2= int(input("gi meg et tall som er mindre enn 100 og delelig med 2?" ))
if (sporsmaal2 < 100) and (sporsmaal2 %2 == 0):
    print("Riktig svar")
elif sporsmaal2 > 100 and sporsmaal2 %2 == 0:
    print("Feil svar, det er delelig med 2 og større enn 100")
else:
    print("Feil svar")
if sporsmaal1 == 1 and sporsmaal2 < 100 and sporsmaal2 %2 == 0:
    print ("Bra", navn,  "du fikk alt riktig")
