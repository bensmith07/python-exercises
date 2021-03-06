# Functions Exercise Walkthroughs

## Exercise 1:
> Define a function named is_two. It should accept one input and return
> `True` if the passed input is either the number `2` or the string `'2'`, 
> and return `False` otherwise.

```python
# the is_two function accepts a single parameter <num> which could be any 
# value, and returns a boolean value based on whether that value is the 
# number 2 or the string '2'
def is_two(val):
    # evaluate the conditional based on whether the passed value is in
    # our list, and return the resulting boolean value of True or False
    return val in [2, '2']
```

Walkthrough: 

1. When we pass the number `2`, the conditional will evaluate to `True`, and 
   the resulting boolean value will be returned and passed to the `print()`
   function. We will see `True` printed in our console/notebook. 

```python
print(is_two(2))
```
```
>>> True
```

2. When we pass the string value `'2'`, we get the same result, since 
   this value is also contained in the list against which the conditional
   statement is checking. 

```python
print(is_two('2'))
```
```
>>> True
```

3. When we pass something else, such as some other number or some other
   string value, the conditional evaluates to `False`, which is then passed
   to our `print()` function and displayed in the console. 

```python
print(is_two(4))
```
```
>>> False
```

```python
print(is_two('New York City'))
```
```
>>> False
```

## Exercise 2

> Define a function named is_vowel. It should return `True` if the passed 
> string is a vowel, `False` otherwise.

```python
# The is_vowel() function accepts a single parameter <letter>, which is 
# expected to be a single-character string. The function will return a 
# boolean value based on whether the character is a vowel.
# We will assume the input will always be a string value.
def is_vowel(letter):
    # Make the input string uppercase, then determine whether it exists
    # in a  list of uppercase vowels. Return the resulting boolean value. 
    return letter.upper() in ['A', 'E', 'I', 'O', 'U']
```

Walkthrough:

1. When we pass letters that are vowels, whether they are uppper or 
   lower case, the conditional evaluates to `True`. That boolean value
   is passed to our `print()` function and displayed in the console. 

```python 
print(is_vowel('a'))
```
```
>>> True
```
```python 
print(is_vowel('E'))
```
```
>>> True
```

2. When we pass some other letter, or a string that is longer than one
   letter, the conditional evaluates to `False`, and the resulting boolean
   is passed to the print function and displayed in the console. 

```python 
print(is_vowel('Z'))
```
```
>>> False
```
```python 
print(is_vowel('Austin, TX'))
```
```
>>> False
```

## Exercise 3

> Define a function named is_consonant. It should return `True` if the 
> passed string is a consonant, `False` otherwise. Use your `is_vowel()` 
> function to accomplish this.

```python
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
```

Walkthrough:

1. If we pass a letter that is a consonant, the letter is first passed to the
   `is_vowel()` function (inside our `is_consonant()` function). This evaluates to 
   `False`, and the `is_consonant()` function returns the opposite, which is `True`. 
   This boolean is passed to our `print()` function and displayed in the console. 

```python
print(is_consonant('B'))
```
```
>>> True
```

2. If we pass a letter that is not a consonant, the opposite happens. The
   `is_vowel()` function evaluates to `True`, and the `is_consonant()` function 
   returns its opposte, `False`. 

```python
print(is_consonant('I'))
```
```
>>> False
```

## Exercise 4

> Define a function that accepts a string that is a word. The 
> function should capitalize the first letter of the word if the 
> word starts with a consonant.

```python
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
```

Walkthrough:

1. When we pass a word to the function whose first letter is a consonant,
   the function will first use our previously defined `is_consonant()` function
   to determine whether the first letter is a consonant. If so, we use the 
   builtin `str.capitalize()` method to capitalize the first letter of the word
   and return the resulting string. This is passed to our `print()` function and 
   displayed in the console. 

```python
print(capitalize('tyrannosaurus'))
```
```
>>> Tyrannosaurus
```

2. Interestingly, we can also pass a string that has more than one word, 
   such as a book title. As long as the first letter of the entire string
   is a consonant, our `str.capitalize()` builtin method will turn the first 
   letter of each word to uppercase and return the resulting string. 

```python
print(capitalize('tyrannosaurus rex goes to college'))
```
```
>>> Tyrannosaurus Rex Goes To College
```

3. However, if we pass a word whose first letter is a vowel, the `is_consonant()`
   function inside our `capitalize()` function will evaluate to `False`. The function 
   will then continue to the `else` clause of our `if` statement, which returns
   the same version of the string that was passed to the `capitalize()` function 
   originally. 

```python
print(capitalize('alamosaurus'))
```
```
>>> alamosaurus
```

## Exercise 5

> Define a function named calculate_tip. It should accept a tip 
> percentage (a number between 0 and 1) and the bill total, and return 
> the amount to tip.

```python
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
```

Walkthrough:

1. In the following code, we use .2 as our first positional argument, and 
   100 as the second. This represents a 20% tip on a $100 check. The two
   values are multiplied together, and the function returns the required
   tip amount of 20. 

```python
print(calculate_tip(.2, 100))
```
```
>>> 20
```

   If we include some f-string formatting, we'll see the output in a more 
   appropriate currency format. 

```python
print(f'${calculate_tip(.2, 100):.2f}')
```
```
>>> $20.00
```

############## ~ Template ~ ##################
## Exercise [exercise number]

> original problem description
> goes here

```python
[function code with comments goes here]
```

Walkthrough:

1. [write your explanation of the code below here]

```python
[demo code here]
```
```
[result of demo code here]
```