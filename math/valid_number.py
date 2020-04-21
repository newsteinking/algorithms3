'''
Validate if a given string can be interpreted as a decimal number.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
" -90e3   " => true
" 1e" => false
"e3" => false
" 6e-1" => true
" 99e2.5 " => false
"53.5e93" => true
" --6 " => false
"-+3" => false
"95a54e53" => false

Note: It is intended for the problem statement to be ambiguous. 
You should gather all requirements up front before implementing one. 
However, here is a list of characters that can be in a valid decimal number:

Numbers 0-9
Exponent - "e"
Positive/negative sign - "+"/"-"
Decimal point - "."
Of course, the context of these characters also matters in the input.
'''


def valid_number(number):
    number = number.strip()
    start, seen_e, seen_dot = 0, False, False
    fraction = False  
    if number[start] in ('+', '-'):
        start += 1

    for i in range(start, len(number)):
        if not number[i].isdigit() and number[i] not in ('e', '.', '+', '-'):
            return False
        else:
            if number[i] in ('+', '-'):
                if i == start or i == len(number)-1: return False 
                if number[i-1] != 'e': return False 
            if number[i] == 'e':
                if i == start or i == len(number)-1: return False 
                if seen_e or fraction: return False
                seen_e = True 
            if number[i] == '.':
                if i == start: fraction = True
                if seen_dot or seen_e: return False
                if i == len(number)-1: return False
                seen_dot = True 

    return True 




