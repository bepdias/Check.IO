# Exercicio: https://py.checkio.org/en/mission/number-factory/


def checkio(num):
    prime_digits = [2, 3, 5, 7]
    factory = []
    original_number = num
    result = 1

    # Como o exercício exige apenas dígitos, fatora o número apenas entre os digitos primos os adiciona a factory
    for i in prime_digits:

        while num % i == 0:
            num = num/i
            factory.append(i)

    # print(num)

    # multiplica todos os números da lista factory
    for x in factory:
        result *= x

    # Garante que se o número for primo ou um de seus divisores for primo com 2 ou mais casas decimais, retorna 0
    if len(factory) == 0 or not result == original_number:
        return 0

    return factory


def function(factory):

    if factory.count(2) >= 2 or factory.count(3) >= 2 or (factory.count(2) >= 1 and factory.count(3) >= 1):
        print("fuck")
    else:
        output = ""

        for x in factory:
            output = output + str(x)
            print(output)


        return int(output)

# TESTE
number = 21
type(function([2,5,7]))
