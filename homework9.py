
def test_param(*params):
    print(*params)

test_param('Serge', 1972, [1, 2, 3, 6])

def factorial_(n):
    if n == 1:
        return 1
    else:
        return n * factorial_(n - 1)

print('Факториал n! =', factorial_(10))

n = int(input('Введите число для определения факториала:'))
print('Факториал для', n, '=', factorial_(n))
