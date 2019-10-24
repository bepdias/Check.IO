# # Exercicio: https://py.checkio.org/en/mission/number-factory/
# Solução achada no google. Incrível criatividade
# https://github.com/yorktsai/checkio/blob/master/electronic-station/number-factory.py

def checkio(data):
    nums = []
    while data > 9:
        found = False

        # Divide continuamente a data pelos dígitos...
        for i in range(9, 1, -1):
            # .... até que a divisão tenha resto zero.
            if data % i == 0:
                found = True
                # Adiciona i a lista
                nums.append(i)
                # Substitui a data pelo inteiro da divisão de data por i
                data = data // i
                # Sai do for.... o while será recomeçado caso o valor de data seja > 9, sempre adicionando um novo número a lista
                break

        # Caso em algum momento num número acima de 9 não seja divisivel por nenhum dígito, é primo. Logo retorna 0
        if found is False:
            return 0

    # Adiciona o dígito restante a lista
    nums.append(data)

    # organiza em ordem crescente para garantir o menor número
    rt = ""
    for num in sorted(nums):
        rt += str(num)

    return int(rt)

data = 135
print(checkio(data))
