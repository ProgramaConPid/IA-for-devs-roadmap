# Clases
# Las clases son plantillas para crear objetos. un objeto es una instancia de una clase

# Ejemplo basico de una clase
class Coche:
  # atributo de clase (comparte todas las instancias)
  tipo = "vehiculo de cuatro ruedas"

  # metodo especial que es el que construye el objeto
  # se llama automaticamente este metodo cuando creas la instancia
  def __init__(self, marca, modelo, color):
    # atributos de la instancia\
    self.marca = marca
    self.modelo = modelo
    self.color = color 

  def arrancar(self):
    print(f"El coche {self.marca} {self.modelo} arranco!")

mi_coche = Coche("Toyota", "Corolla", "rojo")
mi_coche.arrancar()

otro_coche = Coche("Ford", "Fiesta", "Azul")
otro_coche.arrancar()