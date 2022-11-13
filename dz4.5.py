from collections import Counter


def most_com_let():
    word = 'freedom'
    c = Counter(word)
    print(c.most_common(1)[0][0])


most_com_let()
