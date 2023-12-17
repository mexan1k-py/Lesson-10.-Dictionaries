#Homework 1
pets = {}
pets2 = {}

while(True):
    k = input('Введите имя питомца:')
    if k == '':
        break
    else:
        k1 = input('Вид питомца:')
        k2 = int(input('Возраст питомца:'))
        k3 = input('Имя владельца:')
        pets2 = {'Вид питомца:': k1, 'Возраст питомца:': k2, 'Имя владельца:': k3}
        pets[k] = pets2
        for key, value in pets.items():
            vid = value['Вид питомца:']
            vozrast = value['Возраст питомца:']
            name = value['Имя владельца:']
            year = ''
            if vozrast % 10 == 1 and vozrast != 11 and vozrast % 100 != 11:
                year = 'год'
            elif 1 < vozrast % 10 <= 4 and vozrast != 12 and vozrast != 13 and vozrast != 14:
                year = 'года'
            else:
                year = 'лет'
            print(f'Это {vid}, по кличке '
                  f'{key}, Возраст питомца {vozrast} {year}, '
                  f'Имя владельца {name}')

#Homework 2
my_dict = {}

for i in range(20, -11, -1):
    my_dict[i] = i ** i
    print(*my_dict)