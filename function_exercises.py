# 1. Define a function named is_two. It should accept one input and return 
#    True if the passed input is either the number or the string 2, 
#    False otherwise.

def is_two(num):
    if num in [2, '2']:
        return True
    else:
        return False

# 2. Define a function named is_vowel. It should return True if the passed 
#    string is a vowel, False otherwise.

def is_vowel(letter):
    if letter.upper() in ['A', 'E', 'I', 'O', 'U']:
        return True
    else:
        return False

# 3. Define a function named is_consonant. It should return True if the 
# passed string is a consonant, False otherwise. Use your is_vowel 
# function to accomplish this.

def is_consonant(letter):
    if is_vowel(letter):
        return False
    else:
        return True

# 4. Define a function that accepts a string that is a word. The 
#    function should capitalize the first letter of the word if the 
#    word starts with a consonant.

def capitalize(word):
    if is_consonant(word[0]):
        return word.capitalize()
    else:
        return word

# 5. Define a function named calculate_tip. It should accept a tip 
# percentage (a number between 0 and 1) and the bill total, and return 
# the amount to tip.

def calculate_tip(rate, total):
    return rate * total

# 6. Define a function named apply_discount. It should accept a original 
#    price, and a discount percentage, and return the price after the 
#    discount is applied.

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

