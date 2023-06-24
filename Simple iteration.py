from math import exp, sin
from scipy.misc import derivative
'''Цикл у наступній функції переривається, якщо модуль похідної функції не менший за одиницю.
В такому разі программа повертає значення False, а не кортеж із числами, як повинна б була з функцією, що
відповідає вимогам вище. Функцію з експонентою я додав саме для перевірки того, чи може програма визначати
чи відповідає обрана функція вимогам. У випадку з f1(x) = (x ** 2) - exp(x) программа повертає False. 
У випадку з f2 отримуємо кортеж з даними, бо вона відповідає умові роботи методу. Внизу програми стоїть
перевірка типу даних змінної result = iter_method(function, a, b, acc), і якщо в змінну записано тип даних
bool, то друкується повідомлення про невідповідність функції умові. В усьому іншому код відповідний до 
минулих завдань.'''


def iter_method(function, a, b, acc):
    x_0 = (a + b) / 2
    count = 0

    while True:
        if abs(derivative(function, x_0)) > 1:
            return False
        x_1 = x_0
        x_0 = function(x_1)
        count += 1
        if abs(x_0 - x_1) <= acc:
            return x_0, count


def f1(x): return (x ** 2) - exp(x)


def f2(x): return 2 - sin(1 / x)


print('choose an equation to solve with simple iteration method:\n')
print('1) x^2 = exp(x), a = -1, b = 1', '2) x = 2 - sin(1/x), a = 1.2, b = 2', sep='\n')
choice = int(input('enter the number: '))
accuracy = float(input('Enter the needed accuracy: '))
equations = ((f1, -1, 1), (f2, 1.2, 2))
n, m = [_ for _ in equations[choice - 1][1: 3]]

result = iter_method(equations[choice - 1][0], n, m, accuracy)
if type(result) == bool:
    print('Chosen function does not meet the requirements of the method')
else:
    print(f'Root of equation: {result[0]}', f'iterations number: {result[1]}', sep='\n')
