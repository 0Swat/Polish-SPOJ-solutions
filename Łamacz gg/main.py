alfabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']

def Hack(password):
    cracked = ''
    for i in range(0, 20, 2):
        number1 = alfabet.index(password[i])
        number2 = alfabet.index(password[i+1])*16
        cracked += chr(number1+number2)

    print(cracked)

        

def main():
    while True:
        try:
           Hack(str(input())) 
        except:
            break

if __name__ == '__main__':
    main()