__author__ = "Laura Sofia Escobar Cardenas"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "laura.escobarca@campusucc.edu.co"

import CuentaCorriente
from SimuladorBancario import SimuladorBancario

class CDT: 
    #Aqui inicia la declaracion de mi clase 
    ""#----------------------------------------------------
    # Atributos
    #""----------------------------------------------------

    InteresT = 0
    SaldoT = 0
    EstadoT = 0

    ""#----------------------------------------------------
    # Asosiacion 
    ""#----------------------------------------------------

    CuentaCorrienteIngreso= CuentaCorriente()

    ""#----------------------------------------------------
    # Metodos
    ""#----------------------------------------------------}

    __method__ = "DarSaldo"
    __parameter__ = "Ninguno"
    __returns__ = "SaldoT"
    __Description__ = "Metodo que muestra el saldo de la cuenta"
    def DarSaldoT(self):
        # Aqui inicia mi codigo
        return self.SaldoT
    
        __method__ = "DarInteresMensual"
        __parameter__ = "Ninguno"
        __returns__ = "Interes"
        __Description__ = "Metodo que muestra el interes de la cuenta"
    
    def DarInteresMensual(self):
        # Aqui inicia mi codigo
        self.InteresT= self.InteresT*self.SaldoT

    __method__ = "TotalCDT"
    __parameter__ = "Ninguno"
    __returns__ = "Interes"
    __Description__ = "Metodo que calcula el total del saldo"
    def TotalCDT(self):
        # Aqui inicia mi codigo
        self.TotalCDT= self.InteresT + self.SaldoA
        