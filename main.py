
#4. Используйте композицию для создания класса `Zoo`, который будет содержать
# информацию о животных и сотрудниках. Должны быть методы для добавления животных и
# сотрудников в зоопарк.
#5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`,
# которые могут иметь специфические методы (например, `feed_animal()` для `ZooKeeper`
# и `heal_animal()` для `Veterinarian`).

# Создание базового класса
class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print(self.make_sound())

    def eat(self):
        print(self.eat())

# Наследование
class Bird(Animal):
    def make_sound(self):
        print("Kar, Kar")

    def eat(self):
        print("I eat seeds")

class Mammal(Animal):
    def make_sound(self):
        print("Hrr, Hrr")

    def eat(self):
        print("I eat meat")

class Reptile(Animal):
    def make_sound(self):
        print("Shh, Shh")

    def eat(self):
        print("I eat bugs")

class Employee():
    def job(self):
        print(self.job())

class ZooKeeper(Employee):
    def job(self):
        print("I feed animals")

class Veterinarian(Employee):
    def job(self):
        print("I heal animals")


# Композиция
class Zoo():
    def __init__(self, animal, employee):
        self.animal = animal
        self.employee = employee

    def add_habitat(self, animal, employee):
        self.animal.append(animal, employee)

    def remove_habitat(self, animal, employee):
        self.animal.remove(animal, employee)

# Тестирование

bird = Bird("Karkusha", 2)
mammal = Mammal("Kotik", 3)
reptile = Reptile("Tvar", 1)

bird.make_sound()
mammal.make_sound()
reptile.make_sound()

# Демонстрация полиморфизма
animals = [bird, mammal, reptile]
for animal in animals:
    animal.make_sound()

for animal in animals:
    animal.eat()

# Демонстрация композиции
