def answer(text):
    out = ''
    flaga = False
    i = 0
    while i < len(text):
        if text[i] == ' ':
            flaga = True
            i+=1
        else:
            if flaga == True:
                out += text[i].upper()
                i+=1
            else:
                out += text[i]
                i+=1 
            flaga = False
    print(out)


def main():
    while True:
        try:
            text = str(input())
            answer(text)
        except EOFError:
            break

if __name__ == '__main__':
    main()