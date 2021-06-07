# YTLmHWIsBQBU4
global dictionary


def is_valid_word(word: str):
    return word in dictionary


def wordBreak(s: str, result):
    for i in range(1, len(s) + 1):
        first_part = s[:i]
        if is_valid_word(first_part):
            if i == len(s):
                print(result + first_part)
            wordBreak(s[i:], result + first_part + " ")


if __name__ == '__main__':
    dictionary = open('words_alpha.txt', 'r').readlines()
    dictionary = [word.strip() for word in dictionary]
    wordBreak(input().lower().strip().replace(' ', ''), '')
