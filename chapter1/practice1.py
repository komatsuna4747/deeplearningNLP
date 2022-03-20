import random
from typing import Any, List

from nltk.tokenize import sent_tokenize, word_tokenize


def main():
    # Warm-up
    # https://nlp100.github.io/ja/ch01.html
    # Q1
    print("stressed"[::-1])

    # Q2
    word = "パタトクカシーー"
    output = ""
    for i in [0, 2, 4, 6]:
        output += word[i]
    print(output)

    # Q3
    sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
    morph = word_tokenize(sentence)
    morph = [word for word in morph if word.isalnum()]
    print(morph)
    count_morph = [len(word) for word in morph]
    print(count_morph)

    # Q4
    sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
    morph = word_tokenize(sentence)
    morph = [word for word in morph if word.isalnum()]
    list_order = [0, 4, 5, 6, 7, 8, 14, 15, 18]
    output = dict((word[0], i) if i in list_order else (word[0:2], i) for i, word in enumerate(morph))
    print(output)

    # Q5
    def make_n_gram(n: int, list_string: List[str]) -> List:
        return list(zip(*[list_string[i:] for i in range(n)]))

    sentence = "I am an NLPer"
    morph = word_tokenize(sentence)
    words_bi_gram = make_n_gram(2, morph)
    chars_bi_gram = make_n_gram(2, sentence)
    print(words_bi_gram)
    print(chars_bi_gram)

    # Q6
    set_X = set(make_n_gram(2, "paraparaparadise"))
    set_Y = set(make_n_gram(2, "paragraph"))
    union = set_X | set_Y
    intersection = set_X & set_Y
    difference = set_X - set_Y
    print(union)
    print(intersection)
    print(difference)
    print("If X includes se: ", {('s', 'e')} <= set_X)
    print("If Y includes se: ", {('s', 'e')} <= set_Y)

    # Q7
    def make_sentence(x: Any, y: Any, z: Any) -> str:
        return f"{x}時の{y}は{z}"

    print(make_sentence(12, '気温', 22.4))

    # Q8
    def cipher(str):
        rep = [chr(219 - ord(x)) if x.islower() else x for x in str]
        return ''.join(rep)

    sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
    print(cipher(sentence))

    # Q9
    def shuffle_string(sentence: str) -> str:
        output = [
            word[0] + ''.join(random.sample(word[1:-1], len(word[1:-1]))) + word[-1] if len(word) >= 5 else word for word in sentence.split()
            ]

        return ' '.join(output)
    
    print(shuffle_string("I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind."))


if __name__ == "__main__":
    main()
