#Exercício: https://py.checkio.org/en/mission/largest-histogram/

def checkio(data):
    area = len(data)

    for i in range(0, len(data)):
        x = 1
        
        for up in range(1, len(data) - i):
            if data[i + up] >= data[i]:
                x += 1
                # print(x)
            else:
                # print('break')
                break

        for down in range(1, i + 1):
            if data[i - down] >= data[i]:
                x += 1
                # print(x)
            else:
                # print('break')
                break

        if data[i] * x > area:
            area = data[i] * x

    return area

print(checkio([1,2,3,4,0,6,7,8,9]))