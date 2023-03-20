from abc import ABC, abstractmethod

class Persona:
    def __init__(self, nombre='', edad=0):
        self.nombre = nombre
        self.edad = edad

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if isinstance(valor, str):
            self._nombre = valor
        else:
            raise ValueError('El nombre debe ser una cadena de texto.')

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, valor):
        if isinstance(valor, int) and valor >= 0:
            self._edad = valor
        else:
            raise ValueError('La edad debe ser un número entero mayor o igual a cero.')

    def mostrar(self):
        print(f'Nombre: {self.nombre}\nEdad: {self.edad}\nDNI: {self.dni}')

    def es_mayor_de_edad(self):
        return self.edad >= 18


class Cuenta:
    def __init__(self, titular=Persona(), cantidad=0):
        self.titular = titular
        self._cantidad = cantidad

    @property
    def titular(self):
        return self._titular

    @titular.setter
    def titular(self, valor):
        if isinstance(valor, Persona):
            self._titular = valor
        else:
            raise ValueError('El titular debe ser una instancia de la clase Persona.')
    
    @property
    def cantidad(self):
        return self._cantidad
    
    @cantidad.setter
    def cantidad(self, cantidad):
        self._cantidad = cantidad
    
    @abstractmethod
    def mostrar(self):
        print(f"Titular: {self._titular.nombre}, Cantidad: {self._cantidad}")
    
    @abstractmethod
    def ingresar(self, cantidad):
        if cantidad > 0:
            self._cantidad += cantidad
    
    @abstractmethod
    def retirar(self, cantidad):
        pass


class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad, bonificacion=0):
        super().__init__(titular, cantidad)
        self._bonificacion = bonificacion
    
    @property
    def bonificacion(self):
        return self._bonificacion
    
    @bonificacion.setter
    def bonificacion(self, bonificacion):
        self._bonificacion = bonificacion
    
    def es_titular_valido(self):
        edad = self.titular.edad
        return edad >= 18 and edad < 25
    
    
    def retirar(self, cantidad):
        if self.es_titular_valido():
            super().retirar(cantidad)
        else:
            print("No se puede retirar dinero de la cuenta joven. Titular no válido.")

    def ingresar(self, cantidad):
        if self.es_titular_valido():
            super().ingresar(cantidad)
        else:
            print("No se puede ingresar dinero en la cuenta joven. Titular no válido.")
    
    def mostrar(self):
        super().mostrar()
        print(f"Cuenta Joven, Titular: {self._titular.nombre}, Cantidad: {self._cantidad}, Bonificación: {self._bonificacion}")


persona1 = Persona("Mariana Jimenez", 24)
cuenta1 = Cuenta(persona1, 2500)
cuenta2=CuentaJoven(persona1, 3000, 100)
cuenta1.mostrar()
cuenta2.mostrar()
cuenta2.ingresar(200)
cuenta2.mostrar()

