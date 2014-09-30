'''
1.- Fizz Buzz
-If the number is dividable by 3 it returns "fizz"
-If the number is dividable by 5 it returns "buzz"
-If the number is dividable by 15 it returns "fizzbuzz"
'''

def fizzbuzz(num):
    if int(num) % 15 == 0:
        return "fizzbuzz"
    elif int(num) % 5 == 0:
        return "buzz"
    elif int(num) % 3 == 0:
        return "fizz"
    return int(num)

print('If the number is dividable by 3 it\'ll return "fizz", by 5 "buzz", and by 15 "fizzbuzz", otherwise it\'ll return the same number.')
print(fizzbuzz(input("Please choose any number of your liking. ")))
print("")

'''
2.- Prime Factors
Compute the prime factors of a given natural number.
7= [7], 8 = [2,2,2], 4 = [2,2], 6 = [2,3]
'''

def primefactors(orig):
    copy = int(orig)
    primes = []
    while copy != 1:
        for num in range (2, int(orig) +1):
            while copy % num == 0:
                copy = copy // num
                primes.append(num)
    return primes

print(primefactors(input("Please choose a number to get its prime factors. ")))
print("")

'''
3.- Roman Numerals
Convert arabic numbers into roman numbers.
5 = V, 4 = IV, 1829 = MDCCCXXIX
'''

def romannumerals(num):
    if int(num) >= 4000:
        return "Sorry, the number has to be less or equal to 3999."#The official Max roman # is 3,999,999,999
    copy = int(num)
    count = 0
    roman = ""
    while int(copy) >= 1000 and count <= 2:
        count += 1
        roman += "M"
        copy -= 1000
    count = 0######## Count reset
    if int(copy) >= 900:
        roman += "CM"
        copy -= 900
    elif int(copy) >= 800:
        roman += "DCCC"
        copy -= 800
    elif int(copy) >= 700:
        roman += "DCC"
        copy -= 700
    elif int(copy) >= 600:
        roman += "DC"
        copy -= 600
    elif int(copy) >= 500:
        roman += "D"
        copy -= 500
    elif int(copy) >= 400:
        roman += "CD"
        copy -= 400
    while int(copy) >= 100 and count <= 2:
        count += 1
        roman += "C"
        copy -= 100
    count = 0########Count reset
    if int(copy) >= 90:
        roman += "XC"
        copy -= 90
    elif int(copy) >= 80:
        roman += "LXXX"
        copy -= 80
    elif int(copy) >= 70:
        roman += "LXX"
        copy -= 70
    elif int(copy) >= 60:
        roman += "LX"
        copy -= 60
    elif int(copy) >= 50:
        roman += "L"
        copy -= 50
    elif int(copy) >= 40:
        roman += "XL"
        copy -= 40
    while int(copy) >= 10 and count <= 2:
        count += 1
        roman += "X"
        copy -= 10
        count = 0########Count reset
    if int(copy) >= 9:
        roman += "IX"
        copy -= 9
    elif int(copy) >= 8:
        roman += "VIII"
        copy -= 8
    elif int(copy) >= 7:
        roman += "VII"
        copy -= 7
    elif int(copy) >= 6:
        roman += "VI"
        copy -= 6
    elif int(copy) >= 5:
        roman += "V"
        copy -= 50
    elif int(copy) >= 4:
        roman += "IV"
        copy -= 4
    while int(copy) >= 1 and count <= 2:
        count += 1
        roman += "I"
        copy -= 1
    return roman


print(romannumerals(input("Please select a number to transform into roman. (Max # is 3999) ")))
print("")
print("Made by: Luis Raúl Arzola López - A01186956")
