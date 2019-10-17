# Exercício: https://py.checkio.org/en/mission/count-consecutive-summers/

number = 99

s = 0
n_inicial = 1

while n_inicial <= number:
    n = n_inicial
    m = 0

    while n + m < number:
        m += n
        n += 1

    if n + m == number:
        n_inicial += 1
        s += 1

    elif n + m > number:
        n_inicial += 1


print(s)




