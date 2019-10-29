#Exercício: https://py.checkio.org/en/mission/largest-histogram/

def checkio(data):
    area = 1

    for i in range(0, len(data)):
        # x é a quantidade de numeros seguidos que sejam maior ou igual ao central, possibilitando a criação de um retangulo
        x = 1

        # procura acima do numero central
        for up in range(1, len(data) - i):
            if data[i + up] >= data[i]:
                x += 1
                # print(x)
            else:
                # print('break')
                break

        # procura abaixo do numero central
        for down in range(1, i + 1):
            if data[i - down] >= data[i]:
                x += 1
                # print(x)
            else:
                # print('break')
                break

        # confere se o retangulo é o maior até o momento
        if data[i] * x > area:
            area = data[i] * x

    return area

print(checkio([1,2,3,4,0,6,7,8,9]))