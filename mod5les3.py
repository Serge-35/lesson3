class Buiding:
    def __init__(self, namber, b_type):
        self.numberOfFloors = namber
        self.buildingType = b_type

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType

house1 = Buiding(5, 'пятиэтажка')
house2 = Buiding(1, 'одноэтажка')
house3 = Buiding(5, 'пятиэтажка')

print(house1 == house2)
print(house1 == house3)

