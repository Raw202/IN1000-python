from celle import Celle
from spillebrett import Spillebrett

#lager prosedyren main
def main():
    rad = int(input("Hvor mange rader? ")) #tar antall rader fra brukeren 
    kolonne = int(input("Hvor mange kolonner? ")) #tar antall kolonner fra brukeren
    brett = Spillebrett(rad, kolonne) #lager objektet brett
    brett.tegnBrett() #kaller på tegnBrett()
    

    lokke = True
    while lokke:  #lager while løkke
        print("")
        print("Antall levende celler er:", brett.finnAntallLevende())  #print ut antall levende celler i terminalen

        choice = input("Press Enter to continue or q to end the program: ") #spør om brukeren vil fortsatte eller avslutte programmet

        if choice == "":
            brett.oppdatering() #hvis brukere fortsetter, altså skriver enter, skal de kalle på oppdatering metoden
            brett.tegnBrett() #også skal de kalle på tegnBrett metoden
        elif choice == "q": #hvis brukeren avslutter, altså skriver q
            lokke = False #skal while ikke kjøres lenger
        else:
            print("It is not an alternative") #hvis brukeren gir noe annet enn enter eller q, vil det si ikke et alternativ
#kaller på prosedyren
main()
