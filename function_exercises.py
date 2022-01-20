### 1. Define a function named is_two. It should accept one input and return #
###    True if the passed input is either the number or the string 2, 
###    False otherwise.

# the is_two function accepts a single parameter <num> which could be any 
# value, and returns a boolean value based on whether that value is the 
# number 2 or the string '2'
def is_two(val):
    # determine whether the value is the number 2 or the string '2'
    if val in [2, '2']:
        # if so, return True
        return True
    else:
        # otherwise, return False
        return False

### 2. Define a function named is_vowel. It should return True if the passed 
###    string is a vowel, False otherwise.

# The is_vowel() function accepts a single parameter <letter>, which is 
# expected to be a single-character string. The function will return a 
# boolean value based on whether the character is a vowel.
# We will assume the input will always be a string value.
def is_vowel(letter):
    # Make the input string uppercase, then determine whether it matches
    # any character in our list of uppercase vowels.
    if letter.upper() in ['A', 'E', 'I', 'O', 'U']:
        # If so, return True.
        return True
    else:
        # Otherwise, return False.
        return False

### 3. Define a function named is_consonant. It should return True if the 
### passed string is a consonant, False otherwise. Use your is_vowel 
### function to accomplish this.

# The is_consontant() accepts a single parameter <letter>, which is expected
# to be a single-character string. The function will return a boolean value
# based on whether that character is a consonant. We will assume the input
# is a valid string value. 
def is_consonant(letter):
    # Use the previously defined function is_vowel() to determine whether
    # the character is a vowel
    if is_vowel(letter):
        # If it is a vowel, it must not be a consonant, so we return False.
        return False
    else:
        # If it is not a vowel, it is a consonant, so we return True. 
        return True

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

### 6. Define a function named apply_discount. It should accept a original 
###    price, and a discount percentage, and return the price after the 
###    discount is applied.

def apply_discount(price, discount):
    return price * (1 - discount)

# 7. Define a function named handle_commas. It should accept a string 
#    that is a number that contains commas in it as input, and return 
#    a number as output.

def handle_commas(num_string):
    return int(num_string.replace(',', ''))

# 8. Define a function named get_letter_grade. It should accept a number 
#    and return the letter grade associated with that number (A-F).

def get_letter_grade(num):
    if num >= 90:
        return 'A'
    elif num >= 80:
        return 'B'
    elif num >= 70:
        return 'C'
    elif num >= 60:
        return 'D'
    else:
        return 'F'

# 9. Define a function named remove_vowels that accepts a string and 
#    returns a string with all the vowels removed.

def remove_vowels(string1):
    for char in string1:
        if is_vowel(char):
            string1 = string1.replace(char, '')
    return string1

# 10. Define a function named normalize_name. It should accept a string and 
#     return a valid python identifier, that is: 
#     - anything that is not a valid python identifier should be removed
#     - leading and trailing whitespace should be removed
#     - everything should be lowercase
#     - spaces should be replaced with underscores

def normalize_name(string1):

    # convert all letters to lowercase
    string1 = string1.lower()

    #replace spaces with underscores
    string1 = string1.replace(' ', '_')
    
    # remove special characters, leaving only alphanumeric and underscores
    for char in string1:        
        if not char.isalnum() and char != '_':
            string1 = string1.replace(char, '')
    
    # if the first character is a number, remove it
    if string1[0].isdigit():
        string1 = string1.replace(string1[0], '', 1)

    return string1

# 11. Write a function named cumulative_sum that accepts a list of numbers
#     and returns a list that is the cumulative sum of the numbers in the
#     list.

def cumulative_sum(list1):
    sum = 0
    for num in list1:
        sum += num
    sum_list = [sum]
    return sum_list

