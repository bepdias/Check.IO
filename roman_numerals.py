# Exercício: https://py.checkio.org/en/mission/roman-numerals/


# Input: A number as an integer.
#
# Output: The Roman numeral as a string.

UNIDADES = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX','']
DEZENAS = ['X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC','']
CENTENAS = ['C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM','']
MILHARES = ['M', 'MM', 'MMM']


def checkio(num):

    str_num = str(num)

    if len(str_num) == 4:
        first_number = int(str_num[0])
        second_number = int(str_num[1])
        third_number = int(str_num[2])
        fourth_number = int(str_num[3])

        return MILHARES[first_number - 1] + CENTENAS[second_number - 1] + DEZENAS[third_number - 1] + \
               UNIDADES[fourth_number - 1]

    elif len(str_num) == 3:
        first_number = int(str_num[0])
        second_number = int(str_num[1])
        third_number = int(str_num[2])

        return CENTENAS[first_number - 1] + DEZENAS[second_number - 1] + UNIDADES[third_number - 1]

    elif len(str_num) == 2:
        first_number = int(str_num[0])
        second_number = int(str_num[1])

        return DEZENAS[first_number - 1] + UNIDADES[second_number - 1]

    else:
        return UNIDADES[num - 1]

print(checkio(57))