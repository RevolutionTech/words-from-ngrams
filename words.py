import itertools

import enchant
from tqdm import tqdm

from ngrams import get_ngrams_from_csv

NGRAMS_FILENAME = "ngrams.csv"


def permutations(s, max_chars=6):
    return itertools.chain.from_iterable(
        itertools.permutations(s, i) for i in range(2, min(len(s), max_chars) + 1)
    )


def generate():
    ngrams = get_ngrams_from_csv(NGRAMS_FILENAME)
    dictionary = enchant.Dict("en_US")

    for permutation in tqdm(permutations(ngrams.keys())):
        possible_word = "".join(permutation)
        if len(possible_word) <= 6 and dictionary.check(possible_word.lower()):
            print(possible_word)


if __name__ == "__main__":
    generate()
