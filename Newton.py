from math import exp
from scipy.misc import derivative


def newton(function, a, b, acc):
    if function(a) * function(b) >= 0: # перевірка чи існує корінь на відрізку
        print('wrong data (same signs for f(a) and f(b))')
    else:
        if function(a) > function(b): # По факту точку можна визначити рандомно. Я беру ту, що вище осі х
            c = a
        else:
            c = b
        while True:
            diferential = derivative(function, c) # використовуємо функцію знаходж. похідних з scipy
            x_n = c - (function(c) / diferential) # визначаємо точку перетину дотичної з віссю
            if abs(x_n - c) < acc: # умова закінчення циклу
                return x_n
            c = x_n # перевизначаємо точку для проведення дотичної


def f1(x): return (x ** 2) - exp(x)


def f2(x): return (x ** 3) - (4 * x) - 9  # визначаємо функції, корені яких будемо шукати цим методом


print('choose an equation to solve with bisection method:\n')  # вибір з якою функцією працювати
print('1) x^2 = exp(x), a = -1, b = 1', '2) x^3 - 4x - 9 = 0, a = 2, b = 3', sep='\n')

choice = int(input('enter the number: '))
accuracy = float(input('enter the equation error: '))  # Вибір бажаної точності розрахунків

equations = ((f1, -1, 1), (f2, 2, 3))  # вкладений кортеж з функціями, визначеними вище та значеннями точнок а та б

n, m = [_ for _ in equations[choice - 1][1: 3]]  # Дістаємо з кортежу значення точок а та б за допом. спискового
# виразу та зрізу вкладеного кортежу

root = newton(equations[choice - 1][0], n, m, accuracy)  # вираховуємо корінь функцією, визначеною вище
print(f'The root of equation: {root}', f'The F(x) value (x = root) {equations[choice - 1][0](root)}', sep='\n')
# друкуємо значення знайденого кореня та значення функції в цій точці
# часто значення функції f(x) від знайденого нами кореня виводить у форматі 1.793390252302629e-06
