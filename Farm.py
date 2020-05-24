class Animals:
    farm = []
    weight = []
    max_weight = 0
    for maximum in weight:
        if maximum > max_weight:
            max_weight = maximum

    def __init__(self, name, weight, sound):
        self.name = name
        self.weight = weight
        self.sound = sound
        Animals.farm.append(self)
        Animals.weight.append(weight)

    def feed(self):
        self.state = "Кормить"


class Birds(Animals):

    def take_eggs(self):
        self.state = "Собрать яйца"


class Ducks(Birds):
    pass


class Chicken(Birds):
    pass


class Geese(Birds):
    pass


class Artiodactyls(Animals):
    pass


class Give_milk(Artiodactyls):
    def to_milk(self):
        self.state = "Доить"


class Give_wool(Artiodactyls):
    def shearing(self):
        self.state = "Стричь"


duck = Ducks(name='Кряква', weight=3, sound='Кря-кря')
chiken1 = Chicken(name='Ко-Ко', weight=2, sound='кур-кур')
chiken2 = Chicken(name='Кукареку', weight=2, sound='кур-кур')
goose1 = Geese(name='Серый', weight=4, sound='шшшшшш')
goose2 = Geese(name='Белый', weight=5, sound='шшшшшш')
cow = Give_milk(name='Манька', weight=250, sound='Му-му')
goat1 = Give_milk(name='Рога', weight=60, sound='Ме-ме')
goat2 = Give_milk(name='Копыта', weight=70, sound='Ме-ме')
sheep1 = Give_wool(name='Барашек', weight=90, sound='бе-бе')
sheep2 = Give_wool(name='Кудрявый', weight=85, sound='бе-бе')

print(f'Общий вес {sum(Animals.weight)}kg')

for animal in Animals.farm:
    if max(Animals.weight) == animal.weight:
        print(f"Cамое тяжелое животное: {animal.name}")
