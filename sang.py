#klassen Sang med konstruktør og instansvariablene artist og tittel 
class Sang: 
    def __init__(self, artist, tittel):
        
        self._artist = artist.lower()
        self._tittel = tittel.lower() 

#metoden spill() skriver meldingen "Spiller <info om tittel og artist>" ut på terminalen
    def spill(self):
        print (f'Spiller {self._tittel} av {self._artist}')
    
#Metoden returnerer True dersom ett eller flere av navnene i strengen navn finnes i _artist, ellers False.
#jeg bruker split for å splitte ordene for å sikre at metoden fungerer
#bruker lower for at metoden går uansett store bokstaver
    def sjekkArtist(self, navn):
       
        self._navn = navn.lower()
        biter = self._artist.split()
        biter_navn = self._navn.split()
        if True:
            for item in biter_navn:
                if item in biter:
                    return True
        else:
            return False

#Metoden returnerer True om oppgitt tittel er den samme som i instansvariabelen, ellers False
#bruker lower fordi det er uavhengig av små/ store bokstaver.
    def sjekkTittel(self, tittel):
        if tittel.lower() == self._tittel:
            return True
        else:
            return False

#Metoden returnerer True dersom både tittelen og artisten  stemmer med sangens instansvariabler, ellers False
#bruker lower for samme årsaken som før
    def sjekkArtistOgTittel(self, artist, tittel):
        if artist.lower() in self._artist and tittel.lower() in self._tittel:
            return True
        else:
            return False 

#returnerer en ren streng 
    def __str__(self):
        return f'Spiller {self._tittel} av {self._artist}'

