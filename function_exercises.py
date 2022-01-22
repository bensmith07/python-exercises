#############################################################################
### 1. Define a function named is_two. It should accept one input and return #
###    True if the passed input is either the number or the string 2, 
###    False otherwise.

# the is_two function accepts a single parameter <num> which could be any 
# value, and returns a boolean value based on whether that value is the 
# number 2 or the string '2'
def is_two(val):
    # evaluate the conditional based on whether the passed value is in
    # our list, and return the resulting boolean value of True or False
    return val in [2, '2']

#############################################################################
### 2. Define a function named is_vowel. It should return True if the passed 
###    string is a vowel, False otherwise.

# The is_vowel() function accepts a single parameter <letter>, which is 
# expected to be a single-character string. The function will return a 
# boolean value based on whether the character is a vowel.
# We will assume the input will always be a string value.
def is_vowel(letter):
    # Make the input string uppercase, then determine whether it exists
    # in a  list of uppercase vowels. Return the resulting boolean value. 
    return letter.upper() in ['A', 'E', 'I', 'O', 'U']

#############################################################################
### 3. Define a function named is_consonant. It should return True if the 
### passed string is a consonant, False otherwise. Use your is_vowel 
### function to accomplish this.

# The is_consontant() accepts a single parameter <letter>, which is expected
# to be a single-character string. The function will return a boolean value
# based on whether that character is a consonant. We will assume the input
# is a valid string value. 
def is_consonant(letter):
    # Since a letter that is not a vowel must be a consonant,
    # we evaluate whether the letter is a vowel using our previously 
    # defined is_vowel() function. We then use the <not> operator to 
    # return the opposite of the boolean value returned by the is_vowel()
    # function. 
    return not is_vowel(letter)

#############################################################################
### 4. Define a function that accepts a string that is a word. The 
###    function should capitalize the first letter of the word if the 
###    word starts with a consonant.

# The capitalize() function will accept a single parameter <word>, which is
# expected to be a single string value containing words. If the first letter
# of the string is a consonant, the function will return a new version of 
# the string with the first letter of each word capitalized. We will assume
# the input is a valid string value. 
def capitalize(word):
    # Use the previously defined is_consonant() function to determine 
    # whether the first letter of the input string is a consonant.
    if is_consonant(word[0]):
        # If so, use the capitalize() built-in string method to return 
        # a version of the string with the first letter of each word 
        # capitalized.
        return word.capitalize()
    else:
        # Otherwise, return the input string unchanged. 
        return word

#############################################################################
### 5. Define a function named calculate_tip. It should accept a tip 
### percentage (a number between 0 and 1) and the bill total, and return 
### the amount to tip.

# The calculate_tip() function accepts two parameters, which are expected
# to be numbers. The first parameter <rate> is the desired tip percentage
# in the form of a float between 0 and 1. The second parameter <total>
# is the total bill prior to the tip amount being applied. The function 
# will return a float which is the required tip amount. We will assume the 
# inputs are valid number values
def calculate_tip(rate, total):
    # Multiply the tip percentage by the bill total and return the result
    # as the required tip amount
    return rate * total

#############################################################################
### 6. Define a function named apply_discount. It should accept an original 
###    price, and a discount percentage, and return the price after the 
###    discount is applied.

# The apply_discount function accepts two parameters, which are expected to
# be numbers. The first parameter <price> represents the original price of
# an item for purchase, and should be an int or float of any positive value. 
# The second parameter <discount> represents a discount percentage to be 
# applied to the original price, represented by a float between 0 and 1. 
# The function returns a float which represents the price of the item 
# after the discount is applied. We will assume the inputs are valid
# number values. 
def apply_discount(price, discount):
    # Subtract the discount percentage from one, multiply it by the 
    # original price, then return the result. 
    return price * (1 - discount)

#############################################################################
# 7. Define a function named handle_commas. It should accept a string 
#    that is a number that contains commas in it as input, and return 
#    a number as output.

# The handle_commas() function accepts one parameter, which is expected to 
# be a string of digits and comma characters (a whole number represented
# as a string). The function will return a type=int version of that number.
# We will assume the input is a valid string value.
def handle_commas(num_string):
    # Use the string.replace() method to remove all commas by replacing them
    # with empty strings. Then cast that number as an int and return the 
    # result.  
    return int(num_string.replace(',', ''))

#############################################################################
# 8. Define a function named get_letter_grade. It should accept a number 
#    and return the letter grade associated with that number (A-F).

# The get_letter_grade function accepts one parameter, which can be a number
# of any value (float or int). It then returns a string value of a single 
# character which represents the letter grade corresponding to a score of 
# that value. We will assume the input will be a valid number value. 
def get_letter_grade(num):
    # Check whether the value is 90 or greater...
    if num >= 90:
        # If so, return the letter grade 'A'.
        return 'A'
    # Check whether the value is 80 or greater...
    elif num >= 80:
        # If so, return the letter grade 'B'.
        return 'B'
    # Check whether the value is 70 or greater...
    elif num >= 70:
        # If so, return the letter grade 'C'.
        return 'C'
    # Check whether the value is 60 or greater...
    elif num >= 60:
        # If so, return the letter grade 'D'.
        return 'D'
    # If none of the above conditions are met, the grade is below 60...
    else:
        # In which case we return the letter grade 'F'.
        return 'F'

#############################################################################
# 9. Define a function named remove_vowels that accepts a string and 
#    returns a string with all the vowels removed.

# The remove_vowels() function accepts one parameter which is a string,
# removes all vowels from the string, then returns a new version of the 
# string without vowels. We assume the input is a valid string value. 
def remove_vowels(string1):
    # Check each character in the string
    for char in string1:
        # Use the previously defined is_vowel() function to determine
        # whether that character is a vowel. 
        if is_vowel(char):
            # If so, use the builtin replace() method to remove the character
            # by replacing it with an empty string. 
            string1 = string1.replace(char, '')
    # return the resulting string that now has no vowels. 
    return string1

#############################################################################
# 10. Define a function named normalize_name. It should accept a string and 
#     return a valid python identifier, that is: 
#     - anything that is not a valid python identifier should be removed
#     - leading and trailing whitespace should be removed
#     - everything should be lowercase
#     - spaces should be replaced with underscores

# The normalize_name() function is used to turn user input into a valid
# python identifier. It accepts one string parameter and returns a new 
# version of the string with invalid characters removed or replaced. 
# We assume the input will be a valid string value. 
def normalize_name(string1):

    # convert all letters to lowercase using the builtin str.lower() method
    string1 = string1.lower()

    #replace spaces with underscores using the builtin str.replace() method
    string1 = string1.replace(' ', '_')
    
    # remove special characters, leaving only alphanumeric and underscores

    # check each character in the string
    for char in string1:        
        # use the builtin str.isalnum() to check whether character is 
        # alphanumberic. Also check whether the character is an underscore
        if not char.isalnum() and char != '_':
            # if the character is not alphanumeric and is not an underscore,
            # remove it by using the str.replace() method to replace it with 
            # an empty string
            string1 = string1.replace(char, '')
    
    # check whether the first character of the string is a number
    # by indexing it and using the builtin str.isdigit() method
    if string1[0].isdigit():
        # if so, remove it by using the str.replace() method to replace it
        # with an empty string
        string1 = string1.replace(string1[0], '', 1)
    #return the new version of the string
    return string1

#############################################################################
# 11. Write a function named cumulative_sum that accepts a list of numbers
#     and returns a list that is the cumulative sum of the numbers in the
#     list.

# The cumulative_sum() function accepts one parameter, which is expected
# to be a list of numbers. It adds all of those numbers together then returns
# a list containing a single value which is the sum of the numbers in the 
# original list. 
def cumulative_sum(list1):
    # initialize a variable for storing the sum value
    sum = 0
    # check each number in the list
    for num in list1:
        # add that number to the sum variable
        sum += num
    # create a list that contains the sum value
    sum_lst = [sum]
    # return the new list
    return sum_lst

#############################################################################
# BONUS

#############################################################################
# 1.  Create a function named twelveto24. It should accept a string in the 
# format 10:45am or 4:30pm and return a string that is the representation of 
# the time in a 24-hour format. 
   
def twelveto24(time):

    # if the time is between 1:00pm and 9:59pm 
    if time[-2:] == 'pm' and len(time) == 6:
        # get the first digit
        hr_digits = time[0]
        # add 12 to the first digit
        hr_digits = str(int(hr_digits) + 12)

        # concat the remaining characters to the hour digit
        time = hr_digits + time[1:]

    # if the time isbetween 10:00pm and 11:59pm
    elif time[-2:] == 'pm' and time[:2] in ['10', '11']:
        # get the first two digits
        hr_digits = time[:2]
        # add 12 to the first digits
        hr_digits = str(int(hr_digits) + 12)

        # concat the remaining characters to the hour digit
        time = hr_digits + time[2:]
        
    # if the time is between 12:00am and 12:59am
    elif time[-2:] == 'am' and time[:2] == '12':
        # replace the first two digits with '00'
        time = '00' + time[-5:]

    # remove colon and am/pm characters
    time = ''.join(time[:-2].split(':'))

    # if the resulting time is only three digits
    if len(time) == 3:
        # add a zero to the beginning
        time = '0' + time

    return time

#############################################################################
# 1a. Write a function that does the opposite

def twentyfourto12(time):

    # if time between 0000 - 0059
    if time[:2] == '00':
        # change the first two digits to 12, add colon and 'am'
        time = '12' + ':' + time[-2:] + 'am'

    # if time between 0100 - 0959
    elif time[0] == '0':
        # remove the first digit, add colon and 'am'
        time = time[1] + ':' + time[-2:] + 'am'

    # if time between 1000 - 1159:
    elif time[:2] in ['10', '11']:
        # add colon and 'am'
        time = time[:2] + ':' + time[-2:] + 'am'

    # if time between 1200 - 1259
    elif time[:2] == '12':
        # add colon and 'pm'
        time = time[:2] + ':' + time[-2:] + 'pm'

    # if time between 1300 - 2359
    elif int(time[:2]) in range(13, 24):
        # subtract 12 from first two digits, add colon and 'pm
        time = str(int(time[:2]) - 12) + ':' + time[-2:] + 'pm'

    return time

#############################################################################
# 2. Create a function named col_index. It should accept a spreadsheet 
#    column name, and return the index number of the column.
#    col_index('A') returns 1
#    col_index('B') returns 2
#    col_index('AA') returns 27


def col_index(col_name):

    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    col_lst = []

    for letter in alphabet:
        col_lst.append(letter)

    for letter in alphabet:
        for letter2 in alphabet:
            col_lst.append(letter + letter2)

    for letter in alphabet:
        for letter2 in alphabet:
            for letter3 in alphabet:
                col_lst.append(letter + letter2 + letter3)

    return (col_lst.index(col_name)) + 1
        
#############################################################################
