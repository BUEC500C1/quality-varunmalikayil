
from RomanToArabic import RomanToArabic

def test_answer():
    assert RomanToArabic.numberToRoman(1) == 'I'
    assert RomanToArabic.numberToRoman(40000) == 'Number too high, please enter a lower number'
    assert RomanToArabic.numberToRoman(-1) == 'Please enter a valid positive number'
    assert RomanToArabic.numberToRoman(3500) == 'MMMD'
    assert RomanToArabic.numberToRoman(453) == 'CDLIII'
    assert RomanToArabic.numberToRoman(239) == 'CCXXXIX'
    


