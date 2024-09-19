__author__ = "Laura Sofia Escobar Cardenas"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "laura.escobarca@campusucc.edu.co"

from fecha import fecha 


class Empleado: 
    # Aqui inicia la delcaracion de mi clase 

    """#----------------------------------------------------------------------
    # Atributos
    ----------------------------------------------------------------------#"""

    nombre = ""
    apellido = ""
    salario = 0

    """#----------------------------------------------------------------------
    # Masculino = 1   Femenino = 2
    ----------------------------------------------------------------------#"""
    sexo = 0

    """#----------------------------------------------------------------------
    # Asociacion
    ----------------------------------------------------------------------#"""

    fechaIngreso = fecha()
    fechaNacimiento = fecha()

    """#----------------------------------------------------------------------
    # Metodos 
    ----------------------------------------------------------------------#"""

class Fecha: 
    def DarDia():
    # Aqui va mi codigo 
     dia= 0
    
    def DarMes():
    # Aqui va mi codigo 
     mes= 0
    
    def DarAnio():
    # Aqui va mi codigo 
     anio= 0
    
    """#-----------------------------------------------------------------------------------------------------------------
    # Metodos 
    -----------------------------------------------------------------------------------------------------------------#"""
    # este metodo retorna el nombre del empleado 
    
    def DarNombre(self): 
        # Aqui va mi codigo 
        
        __method__ = "CambiarSalario"
        __parameter__ = "nuevosalario"
        __returns__ = "Salario"
        __Description__ = "metodo que actualiza el salario del emmpleado"
        
    def CambiarSalario(self, nuevoSalario):
        # Aqui va mi codigo 
        self.salario = nuevoSalario

    __method__ = "DarSalario"
    __parameter__ = "nuevosalario"
    __returns__ = "Salario"
    __Description__ = ""
        
   