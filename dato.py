#jeg ber brukeren om å gi meg 2 forskjellige datoer
day1 = int(input("Please give me a number of a day  "))
month1 = int(input("Please give me a number of a month "))
day2 = int(input ("Please give me a number of another day "))
month2 = int(input("Please give me a number of another month "))
"""
jeg bruker if-testen for å sjekke hvilken dato kommer først
hvis dato 1 kommer først, er det riktig rekkefølge
det er forskjellige sjanser for at dato1 kommer først
enten det er day1 mindre enn day2, mens mnoth1 mindre eller lik month2
"""
if (day1<day2) and (month1 <= month2):
    print("riktig rekkefølgen")
"""
eller det kan hende at day1 er større eller lik day2
mens month1 er mindre enn month2
"""
elif (day1>=day2) and (month1<month2):
    print ("riktig rekkefølgen")
"""
mens hvis dato 2 kommer frøst, er det feil rekkefølge
det skjer hvis day2 er større eller lik day1 mens month2 er større enn month1
"""
elif (day2>=day1)  and (month2<month1):
    print ("feil rekkefølge")
"""
eller hvis day2 er mindre enn day1 mens month2 er mindre eller lik month1
da blir det feil rekkefølgen
"""
elif (day2<day1) and (month2 <= month1):
    print("feil rekkefølgen")
#hvis brukeren skriver samme dato, blir det samme dato
else:
    print("samme dato")
