s = float(input('Введите сумму кредита: '))
n = int(input('На сколько лет выдан? '))
i = float(input('Сколько процентов годовых? '))


def settlement_calculation(s, i):
    percent = s / 100 * i
    return percent


def loan_body(i, n, s):
    i_1 = i / 100
    k = (i_1 * (1 + i_1) ** n) / (((1 + i_1) ** n) - 1)
    a = k * s
    return round(a, 2)


annual_payment = loan_body(i, n, s)

for payments in range(3):
    print('Остаток долга на начало периода:', s)
    print('Выплачено процентов:', settlement_calculation(s, i))
    print('Выплачено тела кредита:', annual_payment - settlement_calculation(s, i))
    print()
    s -= (annual_payment - settlement_calculation(s, i))

print('Остаток долга:', s)

n_2 = float(input('На сколько лет продляется договор? ')) + (n - 3)
i_2 = float(input('Увеличение ставки до: '))

annual_payment_2 = loan_body(i_2, n_2, s)
for payments_2 in range(int(n_2)):
    print('Остаток долга на начало периода:', s)
    print('Выплачено процентов:', settlement_calculation(s, i_2))
    print('Выплачено тела кредита:', annual_payment_2 - settlement_calculation(s, i_2))
    print()
    s -= (annual_payment_2 - settlement_calculation(s, i_2))

print('Остаток долга:', s)
