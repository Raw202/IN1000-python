#jeg spørrer brukeren om de har lyst på brus, brus er min variabel
#brukeren kan enten svare ja eller nei
brus= input("Har du lyst å drikke brus? ja/nei ")
#jeg bruker if-sjekk for å teste hva brukeren har skrevet inn
if brus == "ja":
    print("Her har du en brus")
elif brus == "nei":
    print("Den er grei.")
else:
    print("Det forstod jeg ikke helt.")
    
