# Доработаем задачи 5-6. Создайте класс-фабрику.
# ○ Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
# ○ Внутри класса создайте экземпляр на основе переданного типа и
# верните его из класса-фабрики.


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

    def making(animal_type, *args, **kwargs):
        set = {'Fish', 'Dog', 'Raven'}
        if animal_type in set:
            if animal_type == 'Fish':
                my_fish = Fish(*args, **kwargs)
                return my_fish
            if animal_type == 'Dog':
                my_dog = Dog(*args, **kwargs)
                return my_dog
            if animal_type == 'Raven':
                my_raven = Raven(*args, **kwargs)
                return my_raven

        else:
            print('Такое животное не производим.')

a = MakeAnimal.making('Fish','Nemo', 2, 'silver', 'bul-bul')
print(a.name, a.age, a.scales, a.voice)
b = MakeAnimal.making('Bird','Nemo', 2, 'silver', 'bul-bul')
