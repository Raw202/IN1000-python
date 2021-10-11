#jeg lager en ordbok med min_varerogpris navn
min_varerogpris={}
#jeg skriver varenavn som nøkkelverdi og pris som innholdsverdi
min_varerogpris={"melk":14.90, "brød":24.90, "yoghurt":12.90, "pizza":39.90}
#jeg skriver ut ordbok ved bruk av print
print(min_varerogpris)
#her ber jeg brukeren om å skrive 2 varenavn med prisen på hver
varenavn1= input("Hva er din favoritt frukt? ")
#jeg bruker lower for å sikre at jeg får varenavn som liten bokstav
#selv om brukeren bruker store bokstaver
varenavn1= varenavn1.lower()
#siden det er pris, jeg bruker float for å få tall som desimaltall
pris1= float(input("Hvor mye koster din favoritt frukt? "))
varenavn2= input("Hva er din favoritt snack? ")
varenavn2=varenavn2.lower()
pris2= float(input("Hvor mye koster din favoritt snack? "))
#her prøver jeg å skrive det brukeren ga som ordbok, nøkkelverdi=innholdsverdi
min_varerogpris[varenavn1]=pris1
min_varerogpris[varenavn2]=pris2
#till slutt skriver jeg ut ordboka 
print(min_varerogpris)
