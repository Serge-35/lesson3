import random
list_ = [i for i in range(3, 21)]
print(list_)
num = random.choice(list_)
print(num)

result = []
for i in range(1, 21):
    for j in range(1, 21):
        if num % (i + j) == 0 and (i, j) not in result and (j, i) not in result and i != j:
            result.append((i, j))
print(*result)



