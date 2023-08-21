# Задание №5
# Создайте три (или более) отдельных классов животных.
# Например рыбы, птицы и т.п.
# У каждого класса должны быть как общие свойства,
# например имя, так и специфичные для класса.
# Для каждого класса создайте метод, выводящий
# информацию специфичную для данного класса.

class Fish():
    def __init__(self, name, age, scales, voice):
        super().__init__(name, age, voice)
        self.scales = scales


    def swim(self):
        print("i'm swimming, oh, it's titan!")


class Dog():
    def __init__(self, name, age, breed, voice):
        super().__init__(name, age, voice)
        self.breed = breed

    def bark(self):
        print('Bark!')


class Raven():
    def __init__(self, name, age, color, voice):
        super().__init__(name, age)
        self.voice = voice
        self.color = name

    def fly_around_corpse(self):
        print('oooh, meat....')

fish = Fish('Nemo', 2, 'silver', 'bul-bul')
dog = Dog('Spark', 5, 'pitbull', 'bark!')
bird = Raven('Qarasique', 6, 'white', 'bravo!')

