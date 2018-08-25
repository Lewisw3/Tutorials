from assets.person import Person


class Man(Person):

    num_of_men = 0

    def __init__(self, name, age, height):
        super().__init__(name, age, 'M', height)
        Man.num_of_men += 1


class Soldier(Person):

    num_of_soldiers = 0

    def __init__(self, name, age, sex, height, unit):
        super().__init__(name, age, sex, height)
        self.unit = unit
        Soldier.num_of_soldiers += 1
