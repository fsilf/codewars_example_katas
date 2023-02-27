# CodeWars Kata Rank04: Roman Numerals Helper
# Create a RomanNumerals class that can convert a roman numeral to and from an integer value.
# See full description of the kata at:
# https://www.codewars.com/kata/51b66044bce5799a7f000003/python  

class RomanNumerals:
    romans = {
        "M": 1000,
        "CM": 900,
        "D": 500,
        "CD": 400,        
        "C": 100,
        "XC": 90,
        "L": 50,
        "XL": 40,
        "X": 10,
        "IX": 9,
        "V": 5,
        "IV": 4,
        "I": 1}

    def to_roman(val):
        roman_num = ""
        for roman_key, roman_val in RomanNumerals.romans.items():
            while (val // roman_val > 0):
                roman_num += roman_key;
                val -= roman_val
        return roman_num;
                    
    def from_roman(s_roman):
        val = 0
        romans = RomanNumerals.romans
        for i in range(len(s_roman)):
            if (i < len(s_roman) - 1) and (romans[s_roman[i]] < romans[s_roman[i+1]]):
                val -= romans[s_roman[i]]
            else:
                val += romans[s_roman[i]]
        return val
