# Exercicio: https://py.checkio.org/en/mission/the-longest-palindromic/

# https://www.geeksforgeeks.org/longest-palindromic-substring-set-2/
# A O(n^2) time and O(1) space program to find the
# longest palindromic substring

# This function prints the longest palindrome substring (LPS)
# of str[]. It also returns the length of the longest palindrome
from pip._vendor.msgpack.fallback import xrange


def checkio(string):
    max_length = 1

    start = 0
    length = len(string)

    # One by one consider every character as center point of
    # even and length palindromes
    for i in range(1, length):
        # Find the longest even length palindrome with center points as i-1 and i.
        low = i - 1
        high = i

        while low >= 0 and high < length and string[low] == string[high]:
            if high - low + 1 > max_length:
                start = low
                max_length = high - low + 1
            low -= 1
            high += 1

        # Find the longest odd length palindrome with center point as i
        low = i - 1
        high = i + 1

        while low >= 0 and high < length and string[low] == string[high]:
            if high - low + 1 > max_length:
                start = low
                max_length = high - low + 1
            low -= 1
            high += 1

    return string[start:start + max_length]


# string = "forgeeksskeegfor"
# print(checkio(string))
