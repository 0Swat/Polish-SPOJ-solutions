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
           return 100
      else:
           return 0
    

def main():
    print(OneRoman2Decimal("M"))
    return

if __name__ == '__main__':
    main()