my_list = ['mango', 'kiwi', 'banana', 'orange', 'appl', 'peach']
print('List: ',my_list)
print('First element: ',my_list[0])
print('Last element: ',my_list[-1])
print('Sublist: ',my_list[2:5])
my_list[2] = 'grape'
print('Modified list: ',my_list)

my_dict = {'mango': 'манго',
         'kiwi': 'киви',
         'banana': 'банан',
         'orange': 'апельсин',
         'appl': 'яблоко',
         'peach': 'персик'}
print('Dictionary:',my_dict)
print(type(my_dict))
print('Translation: ',my_dict['banana'])
my_dict['banana'] = 'БАНАН'
my_dict.update({'pear': 'груша'})
print('Modified dictionary:',my_dict)