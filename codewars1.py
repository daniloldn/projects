def spin_words(sentence):
    word_list = sentence
    y_list = list(word_list.split())
    for i, j in enumerate(y_list):
        if len(j) >= 5:
            y_list[i] = j[::-1]
            continue
    print(' '.join(y_list))
    return y_list



spin_words('seven eleven is amazing')
