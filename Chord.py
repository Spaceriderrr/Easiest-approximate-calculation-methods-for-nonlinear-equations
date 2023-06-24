from math import *  # імпортуємо модуль math для використання експоненти
# такий зпис для того, щоб не писати голову math. перед кожною функцією методу


def chords(function, a, b, acc):  # пишемо функцію для знаходження кореня, в яку включаємо і похибку
    if function(a) * function(b) >= 0:
        print('wrong data (same signs for f(a) and f(b))')  # перевіряємо, що функція, яку рахуємо має різні знаки у
        # точках а та б
    else:
        c1 = a  # фіксуємо точку а, з якої будемо вести відрізок
        while True:
            value_a = function(a)
            value_b = function(b)
            c2 = a - ((value_a * (a - b)) / (value_a - value_b))  # точка перетину відрізку та вісі х
            value_c = function(c2)
            if abs(c1 - c2) < acc:  # умова закінчення нескінч. циклу (довж. відр. менша за похибку)
                return c2
            if (value_a < 0 and value_c > 0) or (value_a > 0 and value_c < 0):  # визначаємо відрізок на якому функція
                # змінює знак і перевизначаємо точки
                b = c2
            else:
                a = c2
            c1 = c2


# Далі копія коду з попереднього завдання
def f1(x): return (x ** 2) - exp(x)


def f2(x): return (x ** 3) - (4 * x) - 9  # визначаємо функції, корені яких будемо шукати цим методом


print('choose an equation to solve with bisection method:\n')  # вибір з якою функцією працювати
print('1) x^2 = exp(x), a = -1, b = 1', '2) x^3 - 4x - 9 = 0, a = 2, b = 3', sep='\n')

choice = int(input('enter the number: '))
accuracy = float(input('enter the equation error: '))  # Вибір бажаної точності розрахунків

equations = ((f1, -1, 1), (f2, 2, 3))  # вкладений кортеж з функціями, визначеними вище та значеннями точнок а та б

n, m = [_ for _ in equations[choice - 1][1: 3]]  # Дістаємо з кортежу значення точок а та б за допом. спискового
# виразу та зрізу вкладеного кортежу

root = chords(equations[choice - 1][0], n, m, accuracy)
print(f'The root of equation: {root}', f'The F(x) value (x = root) {equations[choice - 1][0](root)}', sep='\n')
# друкуємо значення знайденого кореня та значення функції в цій точці
