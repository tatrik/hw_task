"""
Дз "Банкомат":

Стартовые требования.
Есть банкомат:
* Словарь с купюрами вида:
    {номинал: количество, . . . }
* Ф-ция выдачи, то есть мы вызываем эту ф-цию Банкомат.ф-ия(сумма) и нам выводит словарь с купюрами равными этой сумме.
Например:
Ввели 485
Вывело {100:3, 50:3, 20:1, 10:1, 5:1}

Продвинутые требования:
Разработать алгоритм расчета оставшихся купюр так что бы в банкомате их оставалось оптимальное количество(примерно
одинаковое количество номиналов)
"""

atm_copacity = {
    '5': 50,
    '10': 60,
    '20': 55,
    '50': 53,
    '100': 45,
}
rez = dict.fromkeys([5, 10, 20, 50, 100], 0)


def count(s, kwargs):
    while s > 0:
        keys_ATM = list((int(k) for k in kwargs.keys()))
        keys_ATM.reverse()
        n = 1
        for i in keys_ATM:
            if s >= i:
                if kwargs.get(str(i)):
                    rez[i] += n
                    kwargs[str(i)] -= n
                    s -= i
                else:
                    continue
            else:
                continue
    return print(f'give out: {rez} \nBalance at ATM {atm_copacity}')


def withdrawal(s):
    return count(s, atm_copacity)


withdrawal(485)
