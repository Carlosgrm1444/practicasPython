#  # * Explicacion de clase
# lenguaje = "Python"
# print(type(lenguaje)) # ? class str = ""

# lista = [1, 2, 3, 4, 5]
# print(type(lista)) # ? class list = ""

class Dog:
  def __init__ (self, name, age):
    self.name = name
    self.age = age
  
  def bark(self):
    print(f"{self.name} says oof!")

# ? Crear instancias de Dog
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

# ? Imprimir atributos
print(dog1.name)
print(dog2.age)

# ? Llamar al metodo bark
dog1.bark()
dog2.bark()