import math

def numberToRoman (num):
    if(type(num) != int or num < 1):
        return 'Please enter a valid positive number'
    if(num >= 39999):
        return 'Number too high, please enter a lower number'  
    num = int(num)
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

print(numberToRoman(input()))