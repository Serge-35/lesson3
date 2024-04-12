immutable_var = 1, 5, 7, True, 'bcc'
print(immutable_var)
print(type(immutable_var))
print(immutable_var [2])
#immutable_var [2] = 10 #кортеж не поддерживает обращение по элементам.
mutable_list = [2, 4, 6, 8, 'aaa', 'bbb', True]
print(mutable_list)
print(type(mutable_list))
mutable_list[1:4] = [3, 5, 7] #замена в списке 4,6,8
mutable_list [6] = False #замена в списке True на Fals
mutable_list[5] = 'ccc' #замена в списке bbb на ccc
print(mutable_list)