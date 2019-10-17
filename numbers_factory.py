# Exercicio: https://py.checkio.org/en/mission/number-factory/


def checkio(num):
    prime_digits = [2, 3, 5, 7]
    factory = []
    original_number = num
    result = 1

    for i in prime_digits:

        while num % i == 0:
            num = num/i
            factory.append(i)

    # multiplica todos os números da lista factory
    print(num)
    for x in factory:
        result *= x

    if len(factory) == 0 or not result == original_number:
        return 0

    return factory



# TESTE
number = 100000

print(checkio(number))
