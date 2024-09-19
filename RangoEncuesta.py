__author__ = "Laura Sofia Escobar Cardenas"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "laura.escobarca@campusucc.edu.co"

class RangoEncuesta:
    ""#------------------------------------------------
    # Atributos
    ""#------------------------------------------------
    nCasados = 0
    TotalOpinionCasados = 0
    nSolteros = 0
    TotalOpinionSolteros = 0
    ""#------------------------------------------------
    # Metodos 
    ""#------------------------------------------------

    def DarPromedioRango(self):
        TotalOpiniones = (self.TotalOpinionCasados+self.TotalOpinionSolteros)
        TotalEncuestados = (self.nCasados+self.nSolteros)
        return TotalOpiniones/TotalEncuestados
    
    # MetodosSolteros
    def agregarOpinionSoltero(self,nota):
        self.nSolteros+1
        self.TotalOpinionSolteros += nota
    
    def DarPromedioSolteros(self):
        return self.agregarOpinionSoltero/self.TotalOpinionSolteros
    
    def DarNSolteros(self):
        return self.nSolteros
    
    def DarTotalOpinionSolteros(self):
        return self.TotalOpinionSolteros
    
    # MetodosCasados 

    def agregarOpinionCasados(self,nota):
        self.nCasados+1
        self.TotalOpinionCasados += nota
    
    def DarPromedioCasados(self):
        return self.agregarOpinionCasados/self.TotalOpinionCasados
    
    def DarNCasados(self):
        return self.nCasados
    
    def DarTotalOpinionCasados(self):
        return self.TotalOpinionCasados
