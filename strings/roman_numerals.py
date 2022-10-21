# Create a function which accepts a number between 0 & 1000 and return the roman numeral of it.

base_10 = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
romans = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']

def deci_to_roman(num):
    if (num <= 0) or (num > 1000):
        raise ValueError('Numbers below 0 and numbers greater then 1000 are not allowed.')
    
    final = ''

    l = len(romans)-1

    while l>=0:
        d = num//base_10[l]
        num = num%base_10[l]

        while d:
            final += romans[l]
            d -= 1
        
        l -= 1
    
    return final
