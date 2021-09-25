def factorial(n):
    factorial_1 = 1
    for number in range(1, n + 1):
        factorial_1 *= number
    return factorial_1


def degree(x, n):
    count = 1
    for number in range(1, n + 1):
        count *= x
    return count


precision = float(input("Введите точность: "))
x = int(input("Введите икс: "))

addMember = 1
result = 0

n = 0

while abs(addMember) > precision:
    addMember = degree(-1, n) * (degree(x, (2 * n)) / factorial((2 * n)))
    print(addMember)
    result += addMember
    n += 1

print("Сумма ряда =", result)
