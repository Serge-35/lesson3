def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()
print_params(b=25)
print_params(c=[1,2,3])
c = 'не юбилей'
print_params(100, 'дней', c)

values_list = [False, 'Python', 50]
values_dict = {'a': 111,'b': False,'c': 'витамин' }

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [False, 50]
print_params(*values_list_2, 42)
