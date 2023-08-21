# Доработаем задачи 5-6. Создайте класс-фабрику.
# ○ Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
# ○ Внутри класса создайте экземпляр на основе переданного типа и
# верните его из класса-фабрики.
# Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация
# данных), которые вы уже решали. Превратите функции в методы класса, а
# параметры в свойства. Задачи должны решаться через вызов методов
# экземпляра.

class Animal:
    def __init__(self, name, age, voice = 'groal'):
        self.name = name
        self.age = age
        self.voice = voice

    def make_voice(self):
        print(self.voice)

class Fish(Animal):
    def __init__(self, name, age, scales, voice):
        super().__init__(name, age, voice)
        self.scales = scales


    def swim(self):
        print("i'm swimming, oh, it's titan!")

class Dog(Animal):
    def __init__(self, name, age, breed, voice):
        super().__init__(name, age, voice)
        self.breed = breed

    def bark(self):
        print('Bark!')

class Raven(Animal):
    def __init__(self, name, age, color, voice):
        super().__init__(name, age)
        self.voice = voice
        self.color = name

    def fly_around_corpse(self):
        print('oooh, meat....')


class MakeAnimal(Animal):

    set = {'Fish','Dog','Raven'}
    def __init__(self, animal_type, *args, **kwargs):
        if animal_type in set:
            super().__init__(name, age, voice)
            self.animal = animal_type
            return animal
        else:
            print('Такое животное не производим.')

a = MakeAnimal('Fish','Nemo', 2, 'silver', 'bul-bul')
print(a.animal_type)







# fish = Fish('Nemo', 2, 'silver', 'bul-bul')
# dog = Dog('Spark', 5, 'pitbull', 'bark!')
# bird = Raven('Qarasique', 6, 'white', 'bravo!')
#
# animals = [fish, dog, bird]
#
# for i in animals:
#     i.make_voice()
#
# fish.swim()
# dog.bark()
# bird.fly_around_corpse()