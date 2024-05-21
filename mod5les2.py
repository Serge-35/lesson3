class House:
    def __init__(self):
        self.numberOfFloors = 0

    def setNewNumberOfFloors(self):
        floors = int(input('Введите этажность Вашего дома: '))
        self.numberOfFloors = floors

my_house = House()

my_house.setNewNumberOfFloors()
print(my_house.numberOfFloors)
