#jeg bruker prosedyre, jeg ber brukeren om å skrive alder
#jeg bruker int for å sikre at alder gir ett tall
def billett_dyre():
    alder= int(input("Hvor gammel er du? "))
#jeg bruker billetpris som en variabel og gir det verdi lik null
    bilettpris= 0
#her bruker jeg if-testen, hvis alder er mindre eller lik 17
#skal billetprisen være 30, da vil terminalen print hvor mye brukeren betaler
    if alder <= 17:
        billetpris=30
        print("Du skal betale", billetpris)
#hvis alder er mer enn 17 og mindre enn 63 skal prisen være 50
#neste oppgave sier at hvis kjøperen er 63 eller eldre skal prisen være 35
#derfor måtte jeg skrive "and alder mindre enn 63"
    elif alder>17 and alder<63:
        billetpris=50
        print("Du skal betale", billetpris)
#her tester jeg om kjøperen er noe annet skal prisen være 35
    else:
        billetpris=35
        print("Du skal betale", billetpris)
#til slutt kaller jeg prosedyre
billett_dyre()
#Det er ikke noe galt med prosedyre, når jeg skriver 15 får jeg billetpris er 30
#mens når alder er 31 får jeg at billetpris er 50
#når jeg skriver inn 63 får jeg at billetpris er 35. Dvs at prosedyre fungerer
