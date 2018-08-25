from assets.person import Person # from Person is name of the file, import person is the class you are importing


class Woman(Person):

    num_of_woman = 0

    def __init__(self, name, age, height):
        super().__init__(name, age, 'F', height)
        Woman.num_of_woman += 1

