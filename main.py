import math
import random


class Letter:
    def __init__(self, name: str, frequency: float, pos_weights: list):
        self.name = name
        self.frequency = frequency
        self.pos_weights = pos_weights


class Affix:
    def __init__(self, name: str):
        self.name = name
        self.size = len(self.name)


def decides_affix(chance: int) -> list:

    rand_a = random.randint(0, 100)

    bools = [False, False]

    if rand_a < chance:
        bools[0] = True

    rand_b = random.randint(0, 100)

    if rand_b < chance:
        bools[1] = True

    return bools


def get_affixes(prefixes: list, suffixes: list, which_has: list) -> list:

    affixes = [Affix(''), Affix('')]

    if which_has[0]:
        affixes[0] = random.choice(prefixes)

    if which_has[1]:
        affixes[1] = random.choice(suffixes)

    return affixes


def get_random_letter(list_of_letters: list, position: int, sums: list) -> Letter:

    rand = random.randint(0, math.floor(sums[position]) * 100)

    rand /= 100

    for letter in list_of_letters:
        if rand - letter.pos_weights[position] <= 0:
            return letter
        else:
            rand -= letter.pos_weights[position]

    return list_of_letters[4]  # E


def main():
    print("-------------------\nRandom word generator\n--------------------")
    print("This program will try to generate words that feel like they could exist\n")
    print("Note: The method used is very simple and very random, this is not a fancy generator or "
          "anything of the sorts. \nIn more complex cases, some terminations and prefixed come around more often, "
          "but this program doesn't have any of that, it's just a small thing for fun. Hope you enjoy :D\n")
    print("Tip: Try to generate a large number of words to maximize the chance of interesting ones showing up")

    list_of_letters = [
        Letter('a', 0.0805, [5, 12, 8, 8, 8, 10, 8, 5, 3]),
        Letter('b', 0.0183, [5, 0.5, 1.5, 1.5, 1.5, 1, 1.5, 0.5, 0.1]),
        Letter('c', 0.0409, [10, 2.5, 5, 4.5, 4.5, 4, 2.5, 2.5]),
        Letter('d', 0.0344, [5, 1, 2.5, 2.5, 2.5, 2.3, 2.3, 2, 8]),
        Letter('e', 0.1098, [4, 15, 10, 10, 10, 10, 13, 25, 12]),
        Letter('f', 0.0117, [3.75, 0.5, 1.5, 1.5, 1.5, 1, 0.75, 0.4, 0.3]),
        Letter('g', 0.0280, [2.5, 0.1, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 8]),
        Letter('h', 0.0247, [4.5, 4.5, 2.5, 2.5, 2.75, 2.5, 2.5, 1.25, 1.25]),
        Letter('i', 0.0908, [5, 10, 8, 10, 12, 14, 20, 10, 0.1]),
        Letter('j', 0.0018, [1, 0.05, 0.15, 0.12, 0.1, 0.09, 0.01, 0, 0]),
        Letter('k', 0.0082, [5.5, 2.5, 3, 3, 2.75, 2.6, 2.25, 1.25, 2.5]),
        Letter('l', 0.0528, [3, 4.5, 5, 5, 5.5, 5.5, 5, 5.5, 3]),
        Letter('m', 0.0292, [7.5, 2.5, 5, 5, 4, 3.5, 2.5, 1.25, 2.5]),
        Letter('n', 0.0694, [1.5, 7, 5.5, 5.5, 5.5, 5.5, 6, 12, 5]),
        Letter('o', 0.0644, [3, 12, 9, 9, 8.5, 7.5, 8, 7.25, 1]),
        Letter('p', 0.0298, [9, 3, 4, 3.5, 3, 2.25, 1.25, 1, 0.75]),
        Letter('q', 0.0018, [0.55, 0.3, 0.25, 0.2, 0.12, 0.1, 0.75, 0, 0]),
        Letter('r', 0.0707, [5, 7, 7.5, 7, 6.5, 6, 5, 6, 5]),
        Letter('s', 0.0889, [11, 2, 5, 5, 5, 5, 5, 6, 25]),
        Letter('t', 0.0669, [5, 2.5, 6, 6.5, 7, 9, 8.5, 6, 5]),
        Letter('u', 0.0353, [3.5, 6, 3.5, 3.25, 3, 2.75, 2.5, 2.5, 0.01]),
        Letter('v', 0.0096, [1.75, 1, 1.2, 1.1, 1, 0.9, 0.8, 0.8, 0]),
        Letter('w', 0.0072, [4.5, 4.5, 2.5, 2.75, 2.75, 2.75, 2.5, 1.25, 1.25]),
        Letter('x', 0.0028, [0.15, 1, 0.4, 0.25, 0.25, 0.2, 0.25, 0, 0.3]),
        Letter('y', 0.0168, [0.25, 1.5, 0.75, 0.75, 0.75, 0.75, 0.5, 0.25, 5.5]),
        Letter('z', 0.0051, [0.5, 0, 0.25, 0.4, 0.6, 0.75, 1.5, 1, 0])
    ]

    common_prefixes = [
        Affix("dis"),
        Affix("in"),
        Affix("im"),
        Affix("il"),
        Affix("ir"),
        Affix("re"),
        Affix("un"),
        Affix("a"),
        Affix("an"),
        Affix("anti"),
        Affix("auto"),
        Affix("co"),
        Affix("sub"),
        Affix("un")
    ]

    common_suffixes = [
        Affix("ed"),
        Affix("ing"),
        Affix("ly"),
        Affix("s"),
        Affix("es"),
        Affix("er"),
        Affix("en"),
        Affix("ion"),
        Affix("ism"),
        Affix("ity"),
        Affix("ness"),
        Affix("or"),
        Affix("al"),
        Affix("ful"),
        Affix("less")
    ]

    sums = [0] * 9

    for i in list_of_letters:
        for n in range(len(i.pos_weights)):
            sums[n] += i.pos_weights[n]

    chance_affix = 50

    try:
        word_size = int(input("Insert the size of the word you want to generate (max: 9, insert 0 for random"
                              " from 4-7):\n>> "))
        num_word = int(input("Insert how many words you want to generate:\n>> "))
        chance_affix = int(input("Insert how often affixes can appear (0-100, default: 50, higher is usually better)"))
    except ValueError:
        print("Invalid input")
        return

    if word_size > 9 or word_size < 0:
        print("Invalid word size")
        return

    is_random_size = False

    if word_size == 0:
        is_random_size = True

    if num_word <= 0:
        print("Needs a positive number of words to generate")

    for j in range(num_word):
        word = ""

        k = 0

        has_affixes = decides_affix(chance_affix)

        affixes = get_affixes(common_prefixes, common_suffixes, has_affixes)

        prefix = affixes[0]
        suffix = affixes[1]

        if is_random_size:
            word_size = random.randint(4, 7)

        if prefix.size >= word_size - 2:
            has_affixes[0] = False
            prefix = Affix('')

        if suffix.size >= word_size - 2:
            has_affixes[1] = False
            suffix = Affix('')

        if has_affixes[0]:
            word += prefix.name

        if has_affixes[1]:
            k = suffix.size

        for i in range(prefix.size, word_size - k):
            word += get_random_letter(list_of_letters, i - 1, sums).name

        word += suffix.name

        print(word)


if __name__ == "__main__":
    main()
