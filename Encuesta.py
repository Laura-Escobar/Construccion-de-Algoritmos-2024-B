__author__ = "Laura Sofia Escobar Cardenas"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "laura.escobarca@campusucc.edu.co"

from RangoEncuesta import RangoEncuesta

class Encuesta: 
    
    Rango1 = RangoEncuesta()
    Rango2 = RangoEncuesta()
    Rango3 = RangoEncuesta()

def agregarOpinionRangoSolteros(self,nota):
    self.Rango1.agregarOpinionRangoSoltero(nota)

def agregarOpinionRangoCasados(self,nota):
    self.Rango2.agrgarOpinionRangoCasado(nota)

def DarPromedio(self):
    TotalRango1 = self.Rango1.DarTotalOpinionSoltero()+ self.Rango1.DarTotalOpinionSolteros()
    TotalRango2 = self.Rango2.DarTotalOpinionSoltero()+ self.Rango2.DarTotalOpinionSolteros()
    TotalRango3 = self.Rango3.DarTotalOpinionSoltero()+ self.Rango2.DarTotalOpinionSolteros()

    TotalRangos = TotalRango1+TotalRango2+TotalRango3

    TotalEncuestados1 = self.Rango1.DarNCasados+self.Rango1.DarNSolteros()
    TotalEncuestados2 = self.Rango2.DarNCasados+self.Rango2.DarNSolteros()
    TotalEncuestados3 = self.Rango3.DarNCasados+self.Rango3.DarNSolteros()

    TotalEncuestados = TotalEncuestados1+TotalEncuestados2+TotalEncuestados3

    return TotalRangos/TotalEncuestados

def DarPromedioCasados(self): 
    TotalRango1 = self.Rango1.DarTotalOpinionCasados()
    TotalRango2 = self.Rango2.DarTotalOpinionCasados()
    TotalRango3 = self.Rango3.DarTotalOpinionCasados()
    TotalRangosCasados = TotalRango1+TotalRango2+TotalRango3

    TotalCasados1 = self.Rango1.DarNCasados()
    TotalCasados2 = self.Rango2.DarNCasados()
    TotalCasados3 = self.Rango3.DarNCasados()
    TotalCasados= TotalCasados1+TotalCasados2+TotalCasados3

    return TotalRangosCasados/TotalCasados 


