import struct

def printfloat(x_in):
    if x_in == 0:
        print(0, 0, 0, 0)
    else:
        liczba = hex(struct.unpack('<I', struct.pack('<f', x_in))[0])
        wyjscie = []
        wyjscie.append(liczba[2]+liczba[3])
        wyjscie.append(liczba[4]+liczba[5])
        wyjscie.append(liczba[6]+liczba[7])
        wyjscie.append(liczba[8]+liczba[9])
        for i in range(4):
            if wyjscie[i][0] == '0' and wyjscie[i][1] == '0':
                wyjscie[i] = '0'
            elif wyjscie[i][0] == '0' and wyjscie[i][1] != '0':
                wyjscie[i] = wyjscie[i][1] 

        print(wyjscie[0], wyjscie[1], wyjscie[2], wyjscie[3])

t = int(input())
for _ in range(t):
    x = float(input())
    printfloat(x)