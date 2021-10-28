from sang import Sang

#klassen Spilleliste med konstruktør og instansvariabel listenavn 
class Spilleliste:
    def __init__(self, listenavn):
        self._sanger = []
        self._navn = listenavn

#Metoden LesFraFil åpner den oppgitte filen, og leser inn data om sanger på formatet tittel;artist

    def lesFraFil(self, filnavn):


        f = open(filnavn,"r")
        print(f.read())

#bruker strip() for å fjerne tegn for linjeskift på slutten av hver linje
# opprette nye Sang-objekter  og legge disse inn i spillelisten.
        for linje in open(filnavn):
            biter = linje.strip().split(";")
            sang = Sang(biter[1], biter[0])
            self._sanger.append(sang)
 #filen lukkes
        f.close()

#metoden leggTilSang skal legge det nye objektet til spillelisten.
    def leggTilSang(self, nySang):
        self._nySang = nySang
        self._sanger.append(self._nySang)

#metoden fjerner en sang
    def fjernSang(self, sang):
        self._sanger.remove(sang)

 #metoden spiller en sang   
    def spillSang(self, sang):
        self._sang = sang
        print(self._sang) 
                 
#metoden spiller alle sanger
    def spillAlle(self):
       for sang in self._sanger:
            print(sang) 
       
#metoden leter gjennom listen av sanger etter en med oppgitt tittel og returnerer den første den finner.
#Returneres None om tittelen ikke finnes i spillelisten 
    def finnSang(self, tittel):

        for sang in self._sanger:

            if sang.sjekkTittel(tittel) == True:
                return sang
            
        return None
  
#Metoden går gjennom alle sanger i spillelisten og tar vare på de som har en eller flere nav
#fra parameteren artistnavn i navnet på artisten. Disse returneres i en liste med sanger.

    def hentArtistUtvalg(self, artistnavn):
        artistUtValg = []
        for item in self._sanger:
            if item.sjekkArtist(artistnavn):
                artistUtValg.append(item)
            
        return artistUtValg
                