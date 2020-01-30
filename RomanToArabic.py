import math

def numberToRoman (num): 
    romanValues = { 
            1: "I", 
            5: "V", 
            10: "X", 
            50: "L", 
            100: "C", 
            500: "D", 
            1000: "M", 
            5000: "G", 
            10000: "H"
        }

    base = int((10 ** len(str(num))) / 10)
    roman = "" 
  
    while num: 
  
        numOccur = int (num / base) 
  
        if numOccur <= 3: 
            roman += (romanValues[base] * numOccur) 
        elif numOccur == 4: 
            roman += (romanValues[base] + 
                          romanValues[base * 5]) 
        elif 5 <= numOccur <= 8: 
            roman += (romanValues[base * 5] + 
            (romanValues[base] * (numOccur - 5))) 
        elif numOccur == 9: 
            roman += (romanValues[base] +
                         romanValues[base * 10]) 
  
        num = num % base
        base /= 10
          
    return roman 
  
def arabicToNum(arabic):
    dic = { 
        '۰':'0', 
        '١':'1', 
        '٢':'2', 
        '۳':'3', 
        '۴':'4', 
        '۵':'5', 
        '۶':'6', 
        '۷':'7', 
        '۸':'8', 
        '۹':'woo'
    }
    nums = ""
    for i in arabic:
        nums += dic.get(i)
    num = int(nums)
    return num

def arabicToRoman(arabic):
    convert = arabicToNum(arabic)
    return numberToRoman(convert)

print(arabicToRoman(input()))