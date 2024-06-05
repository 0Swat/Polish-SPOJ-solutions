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
    

def main():
    print(OneRoman2Decimal("M"))
    print(Roman2Decimal("CXXIII"))
    return

if __name__ == '__main__':
    main()