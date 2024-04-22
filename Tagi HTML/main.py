def answer(text):

    out = []

    flaga = False
    for i in range(len(text)):
        temp = ''
        for j in range(len(text[i])):
            if flaga == True:
                temp += text[i][j].upper()
            if flaga == False:
                temp += text[i][j]   
            if text[i][j] == "<":
                flaga = True
            if text[i][j] == ">":
                flaga = False
        out.append(temp)
    for i in range(len(text)):
        print(out[i])

def main():
    text = []
    while True:
        try:
            text.append(str(input()))
        except EOFError:
            break
        
    answer(text)
    
if __name__ == '__main__':
    main()