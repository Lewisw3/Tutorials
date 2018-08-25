from assets.man import Man
from assets.man import Soldier
from assets.woman import Woman
from assets.person import Person

peter = Man('Peter', 25, 130)
sandra = Soldier('Sandra', 20, 'W', 120, 'Air Force')
gabi = Woman('Gabi', 24, 165)

if __name__ == '__main__':

    print(peter.name)
    print(sandra.unit)
    print(gabi.height)
    print(peter.num_of_men)
    print(Person.num_of_people)
    print(Soldier.num_of_soldiers)
    print(Person.all_names)


