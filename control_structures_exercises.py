#####################                                                        #                         .
# 1 Conditional Basics 

#    a. Prompt the user for the day of the week, print out whether it   
#       is monday or not. 

day_of_week = input('''Type the day of the week in the following 
format: mon, tue, wed, thu, fri, sat, sun: ''')

if day_of_week == 'mon':
    print('The day of the week is Monday.')
else:
    print('The day of the week is not Monday.') 

#   b. Prompt the user for the day of the week, print out whether it 
#      is a weekday or not. 

day_of_week = str(input('''Type the day of the week in the following 
format: mon, tue, wed, thu, fri, sat, sun: '''))
print()

if day_of_week in ['sat', 'sun']:
    print('It is the weekend.')
else: print('It is a weekday.')
print()

#    c. create variables and make up values for:
#           - the number of hours worked in one week
#           - the hourly rate
#           - how much the week's paycheck will be
## Write the python code that calculates the weekly paycheck. You get
## paid time and a half if you work more than 40 hours

hours_worked = 42
hourly_pay = 14.89
ot_cutoff = 40
ot_rate = 1.5

if hours_worked <= ot_cutoff:
    paycheck = hours_worked * hourly_pay
else:
    paycheck = ((ot_cutoff * hourly_pay)
             + ((hours_worked - ot_cutoff) * hourly_pay * ot_rate))

##############
# LOOP BASICS

#############
# a. WHILE

# Create an integer variable i with a value of 5.
# Create a while loop that runs so long as i is less than or equal to 
# 15. Each loop iteration, output the current value of i, then 
# increment i by one.

i = 5
while i <= 15:
    print(i)
    i += 1

# Create a while loop that will count by 2's starting with 0 and 
# ending at 100. Follow each number with a new line.

i = 0
while i <= 100:
    print(i)
    i += 2

# Alter your loop to count backwards by 5's from 100 to -10.

i = 100
while i >= -10:
    print(i)
    i -= 5

#Create a while loop that starts at 2, and displays the number 
# squared on each line while the number is less than 1,000,000. 

i = 2 
while i < 1_000_000:
    print(i)
    i = i**2

# Write a loop that uses print to create the [given output].

i = 100
while i >= 5:
    print(i)
    i -=5

###########################
# b. FOR LOOPS

# Write some code that prompts the user for a number, then 
# shows a multiplication table up through 10 for that number.

num = input('Enter a whole number: ')
for i in range(1, 11):
    print(num, ' x ', i, ' = ', int(num) * i)

# Create a for loop that uses print to create the [given output]

for i in range(1, 10):
    print(str(i) * i)

###########################
# c. BREAK AND CONTINUE

# Prompt the user for an odd number between 1 and 50. Use a loop 
# and a break statement to continue prompting the user if they 
# enter invalid input. (Hint: use the isdigit method on strings 
# to determine this). Use a loop and the continue statement to 
# output all the odd numbers between 1 and 50, except for the 
# number the user entered.

while True:
    num = input('Enter an odd whole number between 1 and 50: ')
    if num.isdigit():
        num = int(num)
        if num % 2 == 1 and num <= 50:
            break

print('Number to skip is: ', num)
for i in range(1, 50, 2):
    if i != num: 
        print('Here is an odd number: ', i)
        continue
    else:
        print('Yikes! Skipping number: ', i)

# Prompt the user to enter a positive number and write a loop that 
# counts from 0 to that number. (Hints: first make sure that the 
# value the user entered is a valid number, also note that the input 
# function returns a string, so you'll need to convert this to a 
# numeric type.)

while True:
    num = input('Enter a positive whole number: ')
    if num.isdigit():
        break
num = int(num)
for i in range(num + 1):
    print(i)

# alternative solution without break/continue

num = input('Enter a positive whole number: ')
while not num.isdigit():
    num = input('Invalid entry. Enter a positive whole number: ')

num = int(num)

for i in range(num + 1):
    print(i)

# Write a program that prompts the user for a positive integer. 
# Next write a loop that prints out the numbers from the number the 
# user entered down to 1.

while True:
    num = input('Enter a positive whole number: ')
    if num.isdigit():
        break

num = int(num)

for i in range(num, 0, -1):
    print(i)

# alternative solution without break/continue:

num = input('Enter a positive whole number: ')
while (num.isdigit() == False) or (int(num) % 1 != 0) or (int(num) <= 0):
    num = input('Invalid entry. Enter a positive whole number: ')

num = int(num)

for i in range(num, 0, -1):
    print(i)

# 3. Fizzbuzz

# One of the most common interview questions for entry-level programmers is 
# the FizzBuzz test. Developed by Imran Ghory, the test is designed to test 
# basic looping and conditional logic skills.

#    Write a program that prints the numbers from 1 to 100.
#    For multiples of three print "Fizz" instead of the number
#    For the multiples of five print "Buzz".
#    For numbers which are multiples of both three and five print "FizzBuzz".

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)

### 4. Display a table of powers.

###   Prompt the user to enter an integer.
###    Display a table of squares and cubes from 1 to the value entered.
###    Ask if the user wants to continue.
###    Assume that the user will enter valid data.
###    Only continue if the user agrees to.

num = int(input('Enter a positive whole number: '))
input('\nPress Enter to Continue.')
print('\nTable of powers:')
for i in range(1, num + 1):
    print(i, ' ', i**2, i**3)

### BONUS: align the table using string formatting:

# get user input
num = int(input('Enter a positive whole number: '))
input('\nPress Enter to Continue.')

# establish table formatting variables
head1 = 'number'  # heading for first column
head2 = 'squared' # heading for second column
head3 = 'cubed'   # heading for third column
spacer1 = ' | '   # spacer 1, for a divider between columns
spacer2 = '-'     # spacer 2, for a divider under column headings
p = 7             # number of characters to pad

# print the table title
print('\nTable of powers:')

#print the column headings
print(f'{head1:>{p}}{spacer1}\
{head2:>{p}}{spacer1}\
{head3:>{p}}')

# print dividers under the column headings
print(f'{spacer2*(len(head1)):>{p}}{spacer1}\
{spacer2*(len(head2)):>{p}}{spacer1}\
{spacer2*(len(head3)):>{p}}')

# print the contents of the table, with dividers
for i in range(1, num + 1):
    print(f'{i:>{p}}{spacer1}\
{(i**2):>{p}}{spacer1}\
{(i**3):>{p}}')

### alternative method of aligning the table

# get user input
num = int(input('Enter a positive whole number: '))
input('\nPress Enter to Continue.')

# establilsh table formatting variables
head1 = 'number'
head2 = 'squared'
head3 = 'cubed'
spacer = ' | '

# print table title
print('\nTable of powers:')

# print column headings with dividers
print(head1, spacer, head2, spacer, head3)

# print divider under column headings
print('-' * len(head1), spacer, \
      '-' * len(head2), spacer, \
      '-' * len(head3))

#print contents of table, with dividers
for i in range(1, num + 1):
    print(str(i).rjust(len(head1)), spacer, \
          str(i**2).rjust(len(head2)), spacer, \
          str(i**3).rjust(len(head3)))


### 5. Convert given number grades into letter grades.

### Prompt the user for a numerical grade from 0 to 100.
### Display the corresponding letter grade.
### Prompt the user to continue.
### Assume that the user will enter valid integers for the grades.
### The application should only continue if the user agrees to.

score  = int(input('\nEnter a score (0-100): '))
input('\nPress enter to continue.')
if score >= 88:
    print('\nGrade = A')
elif score >= 80:
    print('\nGrade = B')
elif score >= 67:
    print('\nGrade = C')
elif score >= 60:
    print('\nGrade = D')
else:
    print('\nGrade = F')


# Create a list of dictionaries where each dictionary represents a book      
# that you have read. Each dictionary in the list should have the keys 
# title, author, and genre. Loop through the list and print out 
# information about each book.

book_lst = [
    {
        'title': 'Sapiens: A Brief History of Humankind', 
        'author': 'Yuval Noah Harari', 
        'genre': ['non-fiction', 'history']
    },
    {
        'title': 'Brave New World', 
        'author': 'Aldous Huxley',
        'genre': ['science fiction', 'dystopian fiction']
    },
    {
        'title': 'Little and Often: A Memoir', 
        'author': 'Trent Preszler', 
        'genre': ['non-fiction', 'memoir']
    },
    {
        'title': 'The Black Swan: The Impact of the Highly Improbable', 
        'author': 'Nassim Nicholas Taleb', 
        'genre': ['non-fiction']
    },
    {
        'title': 'Educated', 
        'author': 'Tara Westover', 
        'genre': ['non-fiction', 'memoir'] 
    },
    {
        'title': 'Naked Statistics: Stripping the Dread from the Data', 
        'author': 'Charles Wheelan', 
        'genre': ['non-fiction', 'statistics'] 
    }
]

for book in book_lst:
    for key in book:
        if key == 'genre':
            print('genres: ', book['genre'][0])
            for idx in range(1, len(book['genre'])):
                print('\t', book['genre'][idx])
        else:
            print(key, ': ', book[key])
    print()


# Prompt the user to enter a genre, then loop through your books list and 
# print out the titles of all the books in that genre.

genre_lst = []
for book in book_lst:
    for genre in book['genre']:
        if genre not in genre_lst:
            genre_lst.append(genre)

print(genre_lst)
user_genre = input('''Enter a genre from the list above to see 
a list of titles from that genre: ''')

for book in book_lst:
    if user_genre in book['genre']:
        print(book['title'])
