immutable_var = (1, 'Pycharm', False, '523')
print(immutable_var)
#immutable_var[1] = 'Vs code' I 'tuple' object does not... говорит о том, что кортежи не поддаются изменениям)
mutable_list = ["несколько", "элементов", 1, "или", 2]
print(mutable_list)
mutable_list[0] = "several"
mutable_list[1] = "elements"
print(mutable_list)
