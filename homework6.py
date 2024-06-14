my_dict = {
    'John': 1996,
    'Eugene': 1995,
    'Igor': 2005
}

print(my_dict)
print(my_dict.get("Igor"))
print(my_dict.get("Beze", "Такого ключа нет!"))
my_dict.update({'Beze': 1604, 'Nutella': 1946})
print(my_dict.pop('John'))
print(my_dict)

my_set = {777, 666, 'Bara', 'Bara', 'Bara', 'Bere', ('Bere', 'Bere'), 777}
print(my_set)
(my_set.add('Boro'))
(my_set.add('123'))
my_set.remove(666)
print("измененённое множество: ", my_set)
