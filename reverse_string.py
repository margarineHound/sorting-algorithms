def reverse_string(word, word_new):
    if len(word) > 0:
        word_new.append(word[-1])
        reverse_string(word[:-1], word_new)

    return ''.join(word_new)
def reverse_string_loop(word, word_new):
    for i in range(len(word)):
        word_new.append(word[-(i+1)])
    return ''.join(word_new)
def main():

    word = input('enter string: ')
    word_new = []
    word_new = reverse_string(word, word_new)
    print(repr(word_new))
    word_new = []
    word_new = reverse_string_loop(word, word_new)
    print(repr(word_new))

if __name__ == "__main__":
    main()