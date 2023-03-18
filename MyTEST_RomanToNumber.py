

def roman_to_number(x):
    number_s = [1,5,10,50,100,500,1000]
    roman = ['I','V','X','L','C','D','M']

    # y is a holding place for the eventual answer, we'll use it to do all of the calculations within the loop.
    y = 0
    # n will refer always back to the two arrays above: "number_s" and "roman".
    n = 6

# the for loop will take every letter of the roman numeral and check and see if it is one of the 7 characters in the array
    for i in x:
        if i == roman[n]:                
            y = y + number_s[n] # for this code I didn't ever use the shorter version which would be "y += number_s[n]" because doing it the long way helped me think. 
            n = 6 
            # doing this resets n for the next position in x.
            continue
        else:
            n = n - 1
        if i == roman[n]:
            y = y + number_s[n]
            n = 6
            continue
        else:
            n = n - 1
        if i == roman[n]:
            y = y + number_s[n]
            n = 6
            continue
        else:
            n = n - 1
        if i == roman[n]:
            y = y + number_s[n]
            n = 6
            continue
        else:
            n = n - 1
        if i == roman[n]:
            y = y + number_s[n]
            n = 6
            continue
        else:
            n = n - 1
        if i == roman[n]:
            y = y + number_s[n]
            n = 6
            continue
        else:
            n = n - 1
        if i == roman[n]:
            y = y + number_s[n]
            n = 6
            continue
        else:
            n = n - 1
        if i == roman[n]:
            y = y + number_s[n]
            n = 6
            continue
        else:
            n = n - 1
        if i == roman[n]:
            y = y + number_s[n]
            n = 6
            continue
        else:
            n = n - 1
        if i == roman[n]:
            y = y + number_s[n]
            n = 6
            continue
        else:
            n = n - 1
        if i == roman[n]:
            y = y + number_s[n]
            n = 6
            continue
        else:
            n = n - 1
        if i == roman[n]:
            y = y + number_s[n]
            n = 6
            continue
        else:
            n = n - 1
        if i == roman[n]:
            y = y + number_s[n]
            n = 6
            continue
        else:
            n = n - 1
    return y

roman_numeral = input("Enter a roman numeral here: ")

answer = roman_to_number(roman_numeral)


# this is how I chose to account for the subtractions within the logic of roman numeral calculations. 
# the defined function above accounts for each individual letter in the string, so it is necessary to subtract by double the original logic called for. 
if "IV" in roman_numeral:
    answer = answer - 2
if "IX" in roman_numeral:
    answer = answer - 2
if "XL" in roman_numeral:
    answer = answer - 20
if "XC" in roman_numeral:
    answer = answer - 20
if "CD" in roman_numeral:
    answer = answer - 200
if "CM" in roman_numeral:
    answer = answer - 200




            
print("The number is: ",answer)





def number_to_roman(x):
    # to make the calculations easy, an extra 6 positions in the array are added to account for the subtraction logic of roman numerals. 
    number_s = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
    roman = ['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M']
    i = 12
    roman_numeral = ''
    while x != 0:    # I'm running out of time to make my 4 hours so I can explain this logic in person instead of through comments if you'd like (:
        if number_s[i] <= x:
            roman_numeral = roman_numeral + roman[i]
            x = x - number_s[i]
        else:
            i = i - 1
    return roman_numeral

i_number = input("Enter a number here: ")
i_number = int(i_number)
print("The Roman Numeral is: ",number_to_roman(i_number))
