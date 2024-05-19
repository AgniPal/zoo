all_animals = []
# Создание базового класса
class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        all_animals.append(self)

    def make_sound(self):
        print(self.make_sound())

    def eat(self):
        print(self.eat())

    def get_name(self):
        return self.name

    @staticmethod
    def list_animals():
        return [Animal.get_name() for Animal in all_animals]

# Наследование
class Bird(Animal):
    def make_sound(self):
        print("Kar, Kar")

    def eat(self):
        print("I'm bird. I eat seeds")

class Mammal(Animal):
    def make_sound(self):
        print("Hrr, Hrr")

    def eat(self):
        print("I'm mammal. I eat meat")

class Reptile(Animal):
    def make_sound(self):
        print("Shh, Shh")

    def eat(self):
        print("I'm reptile. I eat bugs")

all_employees = []
class Employee():
    def __init__(self, position, name):
        self.position = position
        self.name = name
        all_employees.append(self)

    def job(self):
        print(self.job())

    def get_name(self):
        return self.name
    @staticmethod
    def list_employees():
        return [Employee.get_name() for Employee in all_employees]

class ZooKeeper(Employee):
    def job(self):
        print("I'm ZooKeeper. I feed animals")

class Veterinarian(Employee):
    def job(self):
        print("I'm Veterinarian. I heal animals")


# Композиция
class Zoo():
    def __init__(self, animal, employee):
        self.animal = animal
        self.employee = employee

# Добавление животных и сотрудников в зоопарк
    def add_animal(name,age):
        new_animal = Animal(name, age)
        print(f"Я новичок в зоопарке: {new_animal}")
        return new_animal

    def add_employee(position, name):
        new_employee = Employee(position, name)
        print(f"Я новичок в зоопарке: {new_employee}.")
        return new_employee

# Удаление животных и сотрудников из зоопарка
    def remove_animal(animal):
        if animal in all_animals:
            all_animals.remove(animal)
            print(f"Зоопарк покинул: {animal.get_name()}")
        else:
            print("Такого животного нет в зоопарке")

    def remove_employee(employee):
        if employee in all_employees:
            all_employees.remove(employee)
            print(f"Зоопарк покинул: {employee.get_name()}")
        else:
            print("Такого сотрудника нет в зоопарке")


# Тестирование

bird = Bird("Karkusha", 2)
mammal = Mammal("Kotik", 3)
reptile = Reptile("Tvar", 1)

bird.make_sound()
mammal.make_sound()
reptile.make_sound()

print(Animal.list_animals())

# Демонстрация полиморфизма
animals = [bird, mammal, reptile]
for animal in animals:
    animal.make_sound()

for animal in animals:
    animal.eat()


# Тестирование
employee1 = ZooKeeper("zookeeper", "Vitalik")
employee2 = Veterinarian("veterinarian", "Alex")

print(Employee.list_employees())

employee1.job()
employee2.job()

# Демонстрация полиморфизма
employees = [employee1, employee2]
for employee in employees:
    employee.job()

# Демонстрация композиции

new_animal1 = Zoo.add_animal("Murka", 3)
new_employee2 = Zoo.add_employee("veterinarian", "Oleg")

Zoo.remove_animal(bird)
Zoo.remove_employee(employee2)
