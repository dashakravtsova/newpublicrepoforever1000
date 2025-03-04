user_input = input('Введите температуру (!обязательно укажите шкалу C или F): ')
degree = int(user_input)
if degree[-1] == 'C' or degree[-1] == 'F':
if degree[-1] == 'C':
    print(int(degree[:-1])*1.8+32)
else:
    print((int(degree[:-1])-32)/1.8)
 else:
    print("Ошибка: это совсем не градусы")
    else:
    print("Не та температурная система")