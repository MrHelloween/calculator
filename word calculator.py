

def main():
    text = get_text()

def get_text():
    text = open('text.txt','r')
    text_line = text.read()
    text.close()
    return  text_line

if __name__ == '__main__':
    main()