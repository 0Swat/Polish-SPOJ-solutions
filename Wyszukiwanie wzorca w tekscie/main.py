def TemplateFind(size, template, text):
    text_range = len(text)

    for i in range(text_range - size + 1):
        if text[i:i+size] == template:
            print(i)

def main():
    t = int(input())
    while t:
        size = int(input())
        template = str(input())
        text = str(input())
        TemplateFind(size, template, text)
        t-=1

if __name__ == '__main__':
    main()