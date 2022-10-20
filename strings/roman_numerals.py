# Create a function which accepts a number between 0 & 1000 and return the roman numeral of it.

romans = {
    1:'I',
    4:'IV',
    5:'V',
    9:'IX',
    10:'X',
    50:'L',
    100:'C',
    500:'D',
    1000:'M'
}

def deci_to_roman(num):
    if (num == 0) or (num > 1000):
        raise ValueError('0 and numbers greater then 1000 are not allowed.')
    
