class Buiding:
    total = 0

    def __init__(self):
        Buiding.total += 1

city = []
city_size = 40
while len(city) < city_size:
    new_buiding = Buiding()
    city.append(new_buiding)

print(Buiding.total)
print(city)

