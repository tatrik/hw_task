print('''Команды:
  1 - Наполнить ведро 5л
  2 - Наполнить ведро 3л
  3 - Вылить из ведра 5л
  4 - Вылить из ведра 3л
  5 - Перелить из 5-ти л в 3-х л
  6 -Перелить из 3-х л в 5-ти л''')
V5 = 0
V3 = 0
n = 0
while V5 != 4:
    print('\nВ 5-тилитровом ведре сейчас', V5, 'л')
    print('В 3-хлитровом ведре сейчас', V3, 'л')
    print()
    a = input('Введите команду:')
    if a == '1':
        V5 = 5
        n += 1
    elif a == '2':
        V3 = 3
        n += 1
    elif a == '3':
        V5 = 0
        n += 1
    elif a == '4':
        V3 = 0
        n += 1
    elif a == '5':
        for i in (0, 1, 2, 3, 4, 5):
            if V5 == 0 and V5 == i:
                n += 1
                break
            elif V5 > 0 and i > 0:
                if V5 == i:
                    for j in (0, 1, 2, 3):
                        if V3 == j and j != 3:
                            VS = V5 + V3
                            if VS > 3:
                                V3 = 3
                                V5 = VS - V3
                                n += 1
                                break
                            elif VS <= 3:
                                V3 = VS
                                V5 = 0
                                n += 1
                                break
                        elif V3 == j and j == 3:
                            print('Ведро 3л полное. Выберите другое действие')
                            break
    elif a == '6':
        for k in (0, 1, 2, 3):
            if V3 == 0 and V3 == k:
                n += 1
                break
            elif V3 > 0 and k > 0:
                if V3 == k:
                    for m in (0, 1, 2, 3, 4, 5):
                        if V5 == m and m != 5:
                            VS = V5 + V3
                            if VS > 5:
                                V5 = 5
                                V3 = VS - V5
                                n += 1
                                break
                            elif VS <= 5:
                                V5 = VS
                                V3 = 0
                                n += 1
                                break
                        elif V5 == m and m == 5:
                            print('Ведро 5л полное. Выберите другое действие')
                            n += 1
    else:
        print('Неверное значение!!! Попробуйте снова.')
        continue

print('\nВы справились \n')
print('В 5-тилитровом ведре сейчас', V5, 'л \n')
print('Ваше количество ходов =', n)