class Carro():

    def desplazamiento(self):
        print("Desplazamiento en 4 ruedas")

class Moto():

    def desplazamiento(self):
        print("Desplazamiento en 2 ruedas")

class Camion():

    def desplazamiento(self):
        print("Desplazamiento en 6 ruedas")


def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()

MiVehiculo = Camion() #acá cambiamos la forma!

desplazamientoVehiculo(MiVehiculo)