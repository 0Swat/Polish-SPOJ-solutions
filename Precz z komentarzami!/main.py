def answer_line(data, line, long, long_end, komentarz):
    data_out = ''
    komentarz = False
    for i in range(len(data)):

        if i != len(data)-1:
            tekst = data[i]+data[i+1]

            if tekst == "//":
                line = True
            if tekst == "/*":
                long = True
                komentarz = True

        if line == True:
            data_out += ""
        else:
            if long == True:
                data_out += ""
            else:
                data_out += data[i]

        if long_end == True:
            long = False
            long_end = False

        if i != len(data)-1:
            if tekst == "*/" and long == True:
                long_end = True
                komentarz = False

    
    if data_out != "" or komentarz == False:
        print(data_out)

    return(False, long, long_end, komentarz)


def main():
    line = False
    long = False
    long_end = False
    komentarz = False

    while True:
        try:
            data = str(input())
            line, long, long_end = answer_line(data, line, long, long_end, komentarz)
        except EOFError:
            break

    return

if __name__ == '__main__':
    main()
