from random import randint
from celle import Celle

class Spillebrett:
    def __init__(self, rader, kolonner):
        self._rader = rader
        self._kolonner = kolonner
        self._rutenett = []
        self._generasjonsNum = 0
        for i in range(self._rader):
           self._rutenett.append([])  #lager nøstet liste 
           for j in range(self._kolonner):
               self._rutenett[i].append(Celle()) #Rutenettet skal fylles med et antall Celle-objekter

        self._generer() #kaller på spesiell metode _generer 


    def tegnBrett(self):

        for i in range(4): # for å tømme terminalen
            print()

        print("Generasjon:", str(self._generasjonsNum)) #skriver ut generasjonsnummer på terminalen
#metoden tegnBrett skal bruke en nøstet for-løkke for å skrive ut hvert element i rutenettet
        for element in range(self._rader):
            print()
            for item in range(self._kolonner):
                tegning = self._rutenett[element][item].hentStatusTegn()
                print(tegning, end="")
#metoden oppdatering skal beregne neste generasjon av celler  
    def oppdatering(self):

        doedCellerListe = [] #listen inneholder alle døde celler som skal få status “levende”, 
        levendeCellerListe = []#listen inneholder levende celler som skal få status “død

#gå gjennom rutenettet ved hjelp av en nøstet løkke. For hver celle skal den sjekke om cellen er levende eller død 

        for i in range(self._rader):
            for j in range(self._kolonner):
# henter opp alle naboene til en celle og telle antallet som lever. 
                nabo = self.finnNabo(i, j)
                antallNabo = 0
                for e in nabo:
                    if e.erLevende():
                        antallNabo += 1    
                
                
                if self._rutenett[i][j].erLevende():
                    if antallNabo < 2:      # hvis antall nabo er større enn 2 skal de endre status fra levende til død
                        levendeCellerListe.append(self._rutenett[i][j]) #legger cellen i listen med status død 
                    if antallNabo > 3:
                        levendeCellerListe.append(self._rutenett[i][j])
                    if antallNabo in range(2,4):
                        doedCellerListe.append(self._rutenett[i][j]) 

                if self._rutenett[i][j].erLevende() != True:
                    if antallNabo == 3:
                        doedCellerListe.append(self._rutenett[i][j])
        
        for celle in levendeCellerListe:
            celle.settDoed()  #endre status fra levende til død

        for celle in doedCellerListe:
            celle.settLevende()  #endre status fra død til levende 
#oppdatere telleren for antall generasjoner
        self._generasjonsNum += 1  

#metoden finnAntallLevende skal beregne og returnere antallet levende celler
    def finnAntallLevende(self):
        tall = 0  
#gå gjennom rutenettet og øker en teller for hver levende celle jeg finner.
        for i in range(self._rader):
            for j in range(self._kolonner):
                if self._rutenett[i][j].erLevende():
                    tall += 1
        return tall

#Metoden skal ta imot en celles koordinater (rad og kolonne) i rutenettet og returnere en liste med alle cellens naboer
    def finnNabo(self, rad, kolonne):
        naboerliste = [] #lager tom liste
        for i in range(-1, 2):
            for j in range(-1, 2):
                nabo_rad = rad + i
                nabo_kolonne = kolonne + j
                if (nabo_rad == rad and nabo_kolonne == kolonne) != True:
                    if (nabo_rad < 0 or nabo_kolonne < 0 or nabo_kolonne > self._kolonner -1 or nabo_rad > self._rader - 1) != True:
                        naboerliste.append(self._rutenett[nabo_rad][nabo_kolonne])
        return naboerliste

#metoden gjør at hver celle i rutenettet har ⅓ sjanse for å være levende
    def _generer(self):
        for e in range(self._rader):
            for element in range(self._kolonner):
#metode randint fra klasse Random returnerer et tilfeldig tall fra 0 til o med 3
                tall = randint(0,3)   
                if tall == 3:
                    self._rutenett[e][element].settLevende()
