class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def del_animal(self, name):
        for animal in self.animals:
            if animal.name == name:
                self.animals.remove(animal)
                break

    def show_all_animals(self):
        for animal in self.animals:
            print(f'{animal.name} - {animal.typee} (Возраст: {animal.age})')


class Animal:
    def __init__(self, name, age, typee):
        self.name = name
        self.age = age
        self.typee = typee

    def make_noise(self):
        return 'Noise'


class Mammal(Animal):
    def make_noise(self):
        return 'Noise of monkey'


class Bird(Animal):
    def make_noise(self):
        return 'Noise of bird'


class Fish(Animal):
    def make_noise(self):
        return 'Noise of fish'


zoo = Zoo()

zoo.add_animal(Fish('Сом', 1, 'Рыба'))
zoo.add_animal(Mammal('Обезьяна', 5, 'Млекопитающее'))
zoo.add_animal(Bird('Попугай', 2, 'Птица'))

zoo.show_all_animals()

zoo.del_animal('Попугай')
print("После удаления попугая: \n")
zoo.show_all_animals()



