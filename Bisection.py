from math import *  # імпортуємо модуль math для використання експоненти


def find_value(function, a, b, acc):  # пишемо функцію для знаходження кореня, в яку включаємо і похибку
    if function(a) * function(b) >= 0:  # перевіряємо, що функція, яку рахуємо має різні знаки у точках а та б
        print('wrong data (same signs for f(a) and f(b))')
    else:
        while True:  # Нескінченний цикл, умова переривання якого - знаходження величини 'c', модуль значення функції
            # в якій менший за похибку
            c = (a + b) / 2  # 'ділимо' відрізок
            value_a = function(a)
            value_b = function(b)  # Можна було не оголошувати
            value_c = function(c)  # значення функції у точці перетину
            if abs(value_c) < acc:  # Перевірка чи не менший модуль знач. ф-ції у точці ц за похибку
                return c
            if value_a * value_c < 0:  # Визначення наступного відрізка та зміна значень відповідної точки
                b = c
            else:
                a = c


def f1(x): return (x ** 2) - exp(x)


def f2(x): return (x ** 3) - (4 * x) - 9  # визначаємо функції, корені яких будемо шукати цим методом


print('choose an equation to solve with bisection method:\n')  # вибір з якою функцією працювати
print('1) x^2 = exp(x), a = -1, b = 1', '2) x^3 - 4x - 9 = 0, a = 2, b = 3', sep='\n')

choice = int(input('enter the number: '))
accuracy = float(input('enter the equation error: '))  # Вибір бажаної точності розрахунків

equations = ((f1, -1, 1), (f2, 2, 3))  # вкладений кортеж з функціями, визначеними вище та значеннями точнок а та б

n, m = [_ for _ in equations[choice - 1][1: 3]]  # Дістаємо з кортежу значення точок а та б за допом. спискового
# виразу та зрізу вкладеного кортежу

root = find_value(equations[choice - 1][0], n, m, accuracy)  # вираховуємо корінь функцією, визначеною вище
print(f'The root of equation: {root}', f'The F(x) value (x = root) {equations[choice - 1][0](root)}', sep='\n')
# друкуємо значення знайденого кореня та значення функції в цій точці
