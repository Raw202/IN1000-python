#her lager jeg en ordbok, nøkkelverdi og innholdsverdi
#innholdsverdi har jeg laget som en liste for å skrive 3 måltider
matOrdbok={"rawan":["egg","ris","pølser"],
 "dina":["brød","ost","kylling"],
 "aashild":["ost","pasta","kjøtt"]}
#jeg bruker prosedyre for å be brukeren om å gi meg et navn på beboerne
def beboerne_navn():
     navn= input("Gi meg et navn på en av beboerne! ")
#jeg bruker lower for å få lite bokstaver
     navn= navn.lower()
#jeg bruker if-testen for å teste om brukeren har gitt meg navn rawan
#hvis navnet er rawan, skal det printe ordbok som tilhører til rawan
     if navn== "rawan":
         print (matOrdbok["rawan"])
#hvis navnet er dina, skal det printe ordbok som tilhører til dina
     elif navn== "dina":
         print (matOrdbok["dina"])
#hvis navnet er aashild, skal det printe ordbok som tilhører til aashild
     elif navn== "aashild":
         print (matOrdbok["aashild"])
#hvis navn var noe helt annet, skal det printe beboeren er ikke registert
     else:
         print("Beboeren er ikke registert")
#til slutt kaller jeg prosedyre
beboerne_navn()
#oppgave 3) a) jeg ville bruke mengde, da får vi en samling av ulike brukernavn
#brukernavn er vanligvis unik og det er ikke viktig med ordning
#b)jeg bruker ordbok i dette tilfellet,brukernavn vil være min nøkkelverdi
#antall poeng på innleveringen vil være min innholdsverdi
#c)jeg bruker liste, for da kan jeg få en liste med mange navn
#da er det ok om navn gjentas mange ganer.
#d) jeg ville bruke ordbok, det blir lettere for meg å skrive navn på hver gjest
#som nøkkelverdi og mat de er allergisk mot som en innholdsverdi
