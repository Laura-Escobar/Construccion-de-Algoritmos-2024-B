__author__ = "Laura Sofia Escobar Cardenas"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "laura.escobarca@campusucc.edu.co"

class CuentaAhorros:
    #----------------------------------------------------------------
    # Atributos
    #----------------------------------------------------------------
    __saldo = 0
    __interes = 0
    
    #----------------------------------------------------------------
    # Metodos
    #----------------------------------------------------------------
    __method__ = "DarSaldo"
    __parameter__ = "Ninguno"
    __returns__ = "Saldo de la cuenta"
    __Description__ = "Metodo que muestra el saldo de la cuenta"
    def DarSaldo(self):
        # Aqui inicia mi codigo
        return self.__saldo
    
    __method__ = "ConsignarSaldo"
    __parameter__ = "Monto"
    __returns__ = "Ninguno"
    __Description__ = "Metodo que Permite consignar un monto a la cuenta"
    def ConsignarSaldo(self, monto):
        # Aqui inicia mi codigo
        self.__saldo = self.__saldo+monto
    
    __method__ = "RetirarSaldo"
    __parameter__ = "Monto"
    __returns__ = "Ninguno"
    __Description__ = "Metodo que Permite retirar un monto a la cuenta"
    def RetirarSaldo(self, monto):
        # Aqui inicia mi codigo
        self.__saldo = self.__saldo-monto

    __method__ = "DarInteresMensual"
    __parameter__ = "Ninguno"
    __returns__ = "Interes"
    __Description__ = "Metodo que muestra el interes de la cuenta"
    def DarInteresMensual(self):
        # Aqui inicia mi codigo
        return self.interes 

    __method__ = "actualizarSaldoPorMes"
    __parameter__ = "Ninguno"
    __returns__ = "Saldo"
    __Description__ = "Metodo que actualiza el saldo"
    def actualizarSaldoPorMes(self):
        # Aqui inicia mi codigo
        ""
