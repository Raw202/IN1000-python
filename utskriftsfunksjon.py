#Jeg skriver ut en hilsen til en egen prosedyre.
#Jeg kaller denne prosedyren 3 ganger slik at jeg får lest inn
#og skrevet utinformasjon om 3 personer
#Jeg bruker lower() for å få det brukeren skriver inn som en liten bokstav 
def bruker():
    navn= input("hva heter du? ")
    land= input("hvor kommer du fra? ")
    navn= navn.lower()
    land= land.lower()
    print("Hei", navn, "du er fra", land)
bruker()
bruker()
bruker()
