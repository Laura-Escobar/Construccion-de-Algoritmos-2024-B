__author__ = "Laura Sofia Escobar Cardenas"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "laura.escobarca@campusucc.edu.co"

#----------------------------------------------------------------
# Importaciones
#----------------------------------------------------------------

from CuentaAhorros import CuentaAhorros                                                                                                                      # type: ignore
from CuentaCorriente import CuentaCorriente                                                                                                            # type: ignore
from CDT import CDT                                                                                                                                # type: ignore

class SimuladorBancario:
    
    #----------------------------------------------------------------
    # Atributos
    #----------------------------------------------------------------
    __cedula = ''
    __nombre = ''
    __mesActual = 0
    
    #----------------------------------------------------------------
    # Asociaciones
    #----------------------------------------------------------------
    
    __cuentaAhorros=CuentaAhorros()
    __cuentaCorriente=CuentaCorriente()
    __cdt=CDT()
    #----------------------------------------------------------------
    # Metodos
    #----------------------------------------------------------------
    __method__ = "DepositarCuentaCorriente"
    __parameter__ = "Monto"
    __returns__ = "Ninguno"
    __Description__ = "Metodo que permite depositar en la cuenta corriente"
    def DepositarCuentaCorriente(self, monto):
        # Aqui inicia mi codigo
        self.__cuentaCorriente.ConsignarSaldo(monto)
    
    __method__ = "CalcularSaldoTotal"
    __parameter__ = "Ninguno"
    __returns__ = "Saldo total de todas las cuentas"
    __Description__ = "Metodo que permite calcular el saldo total actual en todas las cuentas"
    def CalcularSaldoTotal(self):
        # Aqui inicia mi codigo
        # Metodo 1
        # total = self.__cuentaCorriente.DarSaldo()+self.__cuentaAhorros.DarSaldo()
        # return total
        # Metodo 2
        return self.__cuentaCorriente.DarSaldo()+self.__cuentaAhorros.DarSaldo()

    __method__ = "DepositarCuentaCorriente"
    __parameter__ = "Monto"
    __returns__ = "Ninguno"
    __Description__ = "metodo que permite depositar en la cuenta corriente"
    def CuentaCorriente(self,Monto):
        # Aqui inicia mi codigo
        self.CuentaCorriente.Depositar(Monto):                                                                                                                   # type: ignore

    __method__ = "CalcularSaldoTotal"
    __parameter__ = "Ninguno"
    __returns__ = "Saldo total de todas las cuentas "
    __Description__ = "metodo que permite depositar en la cuenta corriente"
    def CalcularSaldoTotal(self):
        # Aqui inicia mi codigo 
        # Metodo 1
        # total = self.__CuentaCorriente.DarSaldo()+self.__CuentaAhorros.DarSaldo
        # Total
        # Metodo 2
        Total = self.__cuentaCorriente.DarSaldo() + self.__cuentaAhorros.DarSaldo
    
    __method__ = "PasarAhorroACorriente"
    __parameter__ = "Ninguno"
    __returns__ = "Ninguno"
    __Description__ = "metodo que permite pasar saldo de la cuenta de ahorros"
    def PasarAhorroACorriente(self):
        # Aqui inicia mi codigo
        SaldoAhorros = self.__Cuenta_de_Ahorros.DarSaldo()+self.__cuentaAhorros
        self.__cuentaAhorros.RetirarSaldo(SaldoAhorros)
        self.__cuentaCorriente.ConsignarSaldo(SaldoAhorros)

    __method__ = "Ahorrar"
    __parameter__ = "Ninguno"
    __returns__ = "Ninguno"
    __Description__ = "metodo que permite pasar saldo de la cuenta corriente a la de ahorros"
    def Ahorrar(self,Monto):
        self.__cuentaAhorros = self.__cuenta_de_Ahorros.RetirarSaldo(Monto)
        self.__cuentaCorriente.RetirarSaldo(Monto)
        self.__cuentaAhorros.ConsignarSaldo(Monto)
    __method__ = "RetirarAhorro"
    __parameter__ = "Monto"
    __returns__ = "Ninguno"
    __Description__ = "Retirar un valor dado de la cuenta de ahorros (suponiendo que hay fondos suficientes)"
    def RetirarAhorro(self,Monto):
        self.__cuentaAhorros.RetirarValor(Monto)

    __method__ = "RetirarTodo"
    __parameter__ = "Ninguno"
    __returns__ = "Ninguno"
    __Description__ = "Retirar el valor dado de la cuenta de ahorros el valor que se entrega como parametro (suponiendo que hay fondos suficientes)"
    def RetirarTodo(self):
        self.__cuentaCorriente.RetirarSaldo(self.__cuentaCorriente.DarSaldo())
        self.__cuentaAhorros.RetirarValor(self.__cuentaAhorros.DarSaldo())

    __method__ = "DuplicarAhorro"
    __parameter__ = "Ahorro"
    __returns__ = "Ninguno"
    __Description__ = "duplica la cantidad de dinero que hay en la cuenta de ahorros"
    def DuplicarAhorros(self):
        self.__cuentaAhorros.ConsignarValor(self.__cuentaAhorros.DarSaldo())

    __method__ = "DarSaldoCorriente"
    __parameter__ = "Ninguno"
    __returns__ = "Saldo"
    __Description__ = "retorna saldo que hay en la cuenta corriente"
    def DarSaldoCorriente(self):
        return self.CuentaCorriente.DarSaldo()
    