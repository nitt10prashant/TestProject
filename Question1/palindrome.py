import string
import random


class NegativeNumber(Exception):
    """Defining exception for negative number"""
    pass


class MoreThanTwenty(Exception):
    """Defining exception for integer value more than 20"""
    pass


def rand(type, n):
    """
    :param type: Type can be digit, char, specialchar
    :param N: Integar value
    :return: Random string for give type
    """
    letters = None
    if type == 'digit':
        letters = string.digits
    if type == 'char':
        letters = string.ascii_uppercase
    if type == 'specialchar':
        letters = string.punctuation

    return "".join((random.choice(letters) for _ in range(n)) if letters else letters)


def mod(input_string):
    """
    :param string:given string
    :return: last character and string in input string order without last character
    """
    new, modified_input_string = input_string[-1], input_string[:-1]
    return new, modified_input_string


def palindrome(alphabet_lenth, digit_lenth, specialchar_lenght):
    """
    :param alphabet_lenth: Number of alphabet
    :param digit_lenth: Number of digits
    :param specialchar_lenght: Number of special character
    :return: -1 if polindrome not possible else palindrome string
    """
    index_of_1 = -1
    check = [alphabet_lenth % 2, digit_lenth % 2, specialchar_lenght % 2]
    if 1 in check:
        if check.count(1) > 1:
            return "Input is not valid to create a Palindrome."
        index_of_1 = check.index(1)
    radnom_alphabet_string = rand('char', int(alphabet_lenth/2) + alphabet_lenth % 2)
    radnom_digit_string = rand('digit', int(digit_lenth/2) + digit_lenth % 2)
    radnom_special_char_string = rand('specialchar', int(
        specialchar_lenght/2) + specialchar_lenght % 2)
    if index_of_1 == 0:
        mid_char, radnom_alphabet_string = mod(radnom_alphabet_string)
    elif index_of_1 == 1:
        mid_char, radnom_digit_string = mod(radnom_digit_string)
    elif index_of_1 == 2:
        mid_char, radnom_special_char_string = mod(radnom_special_char_string)
    else:
        mid_char = ""
    Halfstring = radnom_alphabet_string + radnom_digit_string + radnom_special_char_string
    random.shuffle(list(Halfstring))
    randomized_halfstring = "".join(Halfstring)
    return randomized_halfstring + mid_char + randomized_halfstring[::-1]

def validate_input(input_type, iter=3):
    num = None
    print ("Enter {} lenght in integer".format(input_type))
    while iter > 0:
        iter -= 1
        try:
            num = int(input())
            if num > 20:
                num = None
                raise MoreThanTwenty
            if num < 0:
                num = None
                raise NegativeNumber
            break
        except ValueError:
            print("entered value is not an integer try again")
        except NegativeNumber:
            print (
                "Entered value is negative number please enter positive integer number")
            continue
        except MoreThanTwenty:
            print("Entered value is more than 20 please enter < 20")
    if num is None:
        print ("Exceeded number of retry for the input")
        exit()
    return num


if __name__ == '__main__':
    print ("This program generates palindrome string for given user input. \nInstructions for the inputs:\n 1-All the values should be integer\n 2-Maximum string size should be <=20\n 3:Max try for an input is 3")
    input("If you want to generate palindrome and understood the input guideline. \nPress Enter to continue...")
    string_lenght = validate_input("string")
    if string_lenght > 20 or string_lenght == 0:
        print ("string lenght must be 0 <= sting <= 20")
        exit()
    char_lenght = validate_input("char")
    digit_lenthit_lenght = validate_input("digit_lenthit")
    specialchar_lenghtchar_lenght = validate_input("specialchar_lenght char")
    if string_lenght < char_lenght + digit_lenthit_lenght + specialchar_lenghtchar_lenght:
        print ("Given string lenght is less than sum individual input lenght")
        exit()
    elif string_lenght > char_lenght + digit_lenthit_lenght + specialchar_lenghtchar_lenght:
        print ("Given string lenght is more than sum of individual input lenght")
        exit()
    else:
        palindrom_string = palindrome(
            alphabet_lenth=char_lenght, digit_lenth=digit_lenthit_lenght, specialchar_lenght=specialchar_lenghtchar_lenght)
        print (palindrom_string)
