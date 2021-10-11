#Jeg skriver et program med en variabel som er temperatur i fahrenheit
#og jeg bestemmer at temp er 50
tempfahr= 50
print("Tempraturen i fahrenheit er", tempfahr)
#Jeg definerer en ny variabel for å finne temperaturen i celsius.
tempCels= int((tempfahr-32)*5/9)
print("Tempraturen i celsius er", tempCels)
#Jeg modifiserer programmet slik at variabelen for fahrenheit
#blir gitt via brukerinput.
tempfahr=int(input("Hva er tempraturen i Oslo nå? "))
print("Temprautren i Oslo nå er", tempfahr, "i fahrenheit")
tempCels= (tempfahr-32)*5/9
#Jeg bruker round for å sikre at jeg får bare to desimaler
tempCels= round(tempCels, 2)
#Til slutt skriver jeg ut temp i celsius som brukeren bestemte
print("Tempraturen i Oslo nå er", tempCels, "i celsius")
