def formula(x):
    return (x ** 3) - (3 * x ** 2) - 12 * x + 10


hazard_level = float(input('Введите максимально допустимый уровень опасности:'))

minimum_depth = 0
maximum_depth = 4

middle = minimum_depth + (maximum_depth - minimum_depth) / 2
lvl_danger = formula(middle)

while abs(lvl_danger) > hazard_level:
    if lvl_danger > 0:
        minimum_depth = middle
    else:
        maximum_depth = middle
    middle = minimum_depth + (maximum_depth - minimum_depth) / 2
    lvl_danger = formula(middle)

print('Приблизительная глубина безопасной кладки:', middle)