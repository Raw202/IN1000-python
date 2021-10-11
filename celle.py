class Celle:
   # Konstruktør
    def __init__(self):
        
        self._celleStatus = "død" 

    # Endre status
    def settDoed(self):
        self._celleStatus = "død"

    def settLevende(self):
        self._celleStatus = "levende"

    # Hente status
    def erLevende(self):
        
        if self._celleStatus == "levende":
            return True
        else: 
            return False
    
    # returnerer en tegnrepresentasjon

    def hentStatusTegn(self):
        if self._celleStatus == "levende":
            return "O"
        else: 
            return "."