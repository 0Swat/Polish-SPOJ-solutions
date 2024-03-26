def CzyPalindrom(a):
    liczba_str = str(a)
    for i in range(len(liczba_str)):
        if liczba_str[i] != liczba_str[len(liczba_str)-i-1]:
            return False
    return True
   
def ZnajdzPalindrom(a):
    liczba_dodawan = 0
    while(CzyPalindrom(a)==False):
        palindrom = str(a)
        palindrom_tyl = ''
        for i in range(len(palindrom)):
            palindrom_tyl += palindrom[len(palindrom)-i-1]
        a = a + int(palindrom_tyl)
        liczba_dodawan+=1
    print(a, liczba_dodawan)

t = int(input())
while t:
    a = int(input())
    ZnajdzPalindrom(a)
    t-=1