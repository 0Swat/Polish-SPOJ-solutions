def OneRoman2Decimal(roman):
      if roman == "I":
           return 1
      elif roman == "V":
           return 5
      elif roman == "X":
           return 10
      elif roman == "L":
           return 50
      elif roman == "C":
           return 100
      elif roman == "D":
           return 500
      elif roman == "M":
           return 1000
      else:
           return 0
      
def Roman2Decimal(roman):
    return_sum = 0

    for i in range(len(roman)-1):
        if OneRoman2Decimal(roman[i]) >= OneRoman2Decimal(roman[i+1]):
            return_sum += OneRoman2Decimal(roman[i])
        else:
            return_sum -= OneRoman2Decimal(roman[i])
    return_sum += OneRoman2Decimal(roman[len(roman)-1])

    return return_sum

def OneDecimal2Roman(decimal):
    if decimal >= 1000:
         return "M"
    elif decimal >= 900:
         return "CM"
    elif decimal >= 500:
         return "D"
    elif decimal >= 400:
         return "CD"
    elif decimal >= 100:
         return "C"
    elif decimal >= 90:
         return "XC"
    elif decimal >= 50:
         return "L"
    elif decimal >= 40:
         return "XL"
    elif decimal >= 10:
         return "X"
    elif decimal >= 9:
         return "IX"
    elif decimal >= 5:
         return "V"
    elif decimal >= 4:
         return "IV"
    elif decimal >= 1:
         return "I"
    else:
         return ""
    
def Decimal2Roman(decimal):
    
    decimal_number = decimal
    return_roman = ""

    while decimal_number:
         return_roman += OneDecimal2Roman(decimal_number)
         decimal_number -= Roman2Decimal(OneDecimal2Roman(decimal_number))

    return return_roman
         
    
    

def main():
    print(OneRoman2Decimal("M"))
    print(Roman2Decimal("CXXIII"))
    print(OneDecimal2Roman(960))
    print(Decimal2Roman(1461))
    return

if __name__ == '__main__':
    main()