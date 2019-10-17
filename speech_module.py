# Exercício: https://py.checkio.org/en/mission/speechmodule/
#
# import inflect
#
# p = inflect.engine()
#
#
# def checkio(number):
#     number_to_word = p.number_to_words(number)
#
#     return number_to_word
#
#
# print(checkio(101))


# //////////////////////////////////////////////////////////////////////////
# CHECKIO NÃO PERMITE USAR INFLECT, ENTÃO AQUI ESTÁ A OUTRA SOLUÇÃO
import math

FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def first_digit(number):

    digits = int(math.log10(number))

    number = int(number / pow(10, digits))

    return number


def checkio(number):

    size = len(str(number))

    if size == 1:
        return FIRST_TEN[number-1]

    elif size == 2:
        if first_digit(number) == 1:
            return SECOND_TEN[number % 10]
        elif number % 10 == 0:
            return OTHER_TENS[first_digit(number) - 2]
        else:
            return OTHER_TENS[first_digit(number) - 2] + " " + FIRST_TEN[number % 10 - 1]

    else:
        str_number = str(number)
        second_digit = int(str_number[1])

        if number % 10 == 0 and second_digit == 0:
            return FIRST_TEN[first_digit(number) - 1] + " " + HUNDRED

        elif second_digit == 0:
            return FIRST_TEN[first_digit(number) - 1] + " " + HUNDRED + " " + FIRST_TEN[number % 10 - 1]

        elif second_digit == 1:
            return FIRST_TEN[first_digit(number) - 1] + " " + HUNDRED + " " + SECOND_TEN[number % 10]

        elif number % 10 == 0:
            return FIRST_TEN[first_digit(number) - 1] + " " + HUNDRED + " " + OTHER_TENS[second_digit - 2]

        else:
            return FIRST_TEN[first_digit(number) - 1] + " " + HUNDRED + " " + OTHER_TENS[second_digit - 2] + " " + \
                   FIRST_TEN[number % 10 - 1]



print(checkio(587))