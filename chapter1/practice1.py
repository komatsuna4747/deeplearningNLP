import nltk

def main():
    # Warm-up
    # Q1
    print('stressed'[::-1])

    # Q2
    word = 'パタトクカシーー'
    output = ''
    for i in [0, 2, 4, 6]:
        output += word[i]
    print(output)

    # Q3
    sentence = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
    morph = nltk.word_tokenize(sentence)
    print(morph)


if __name__ == '__main__':
    main()