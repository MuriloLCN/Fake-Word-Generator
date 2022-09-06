import math
import random


class Letter:
    def __init__(self, name: str, frequency: float, pos_weights: list):
        self.name = name
        self.frequency = frequency
        self.pos_weights = pos_weights


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

    sums = [0] * 9

    for i in list_of_letters:
        for n in range(len(i.pos_weights)):
            sums[n] += i.pos_weights[n]

    try:
        word_size = int(input("Insert the size of the word you want to generate:\n>> "))
        num_word = int(input("Insert how many words you want to generate:\n>> "))
    except ValueError:
        print("Invalid input")
        return

    if word_size > 9 or word_size <= 0:
        print("Invalid word size")
        return

    if num_word <= 0:
        print("Needs a positive number of words to generate")

    for j in range(num_word):
        word = ""

        for i in range(word_size):
            word += get_random_letter(list_of_letters, i - 1, sums).name

        print(word)


if __name__ == "__main__":
    main()
