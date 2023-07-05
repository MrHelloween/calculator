def main():
    text = get_text()
    get_words(text)


def get_text():
    text = open('text.txt', 'r')
    text_line = text.read()
    text.close()
    return text_line


def get_words(text):
    list_words = text.split()
    delete_back = ['.', ',', '?', ':', '!', ')','"']
    delete_frond = ['(', '"']
    new_list = []
    for i in list_words:
        if i[-1] in delete_back:
            new_list.append(i[:-1])
        elif i[0] in delete_frond:
            new_list.append(i[1:])
        else:
            new_list.append(i)
    print(new_list)


if __name__ == '__main__':
    main()
