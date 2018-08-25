class Person:

    num_of_people = 0
    all_names = []

    def __init__(self, name, age, sex, height):
        # initialise instance attributes
        self.name = name
        self.age = age
        self.sex = sex
        self.height = height

        # update class attributes
        Person.num_of_people += 1
        Person.all_names.append(self.name)
