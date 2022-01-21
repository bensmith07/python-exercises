# Functions Exercise Walkthroughs

## Exercise 1:
> Define a function named is_two. It should accept one input and return
> True if the passed input is either the number or the string 2, False
> otherwise.

```python
# the is_two function accepts a single parameter <num> which could be any 
# value, and returns a boolean value based on whether that value is the 
# number 2 or the string '2'
def is_two(val):
    # evaluate the conditional based on whether the passed value is in
    # our list, and return the resulting boolean value of True or False
    return val in [2, '2']
```

### Walkthrough: 

1. When we pass the number 2, the conditional will evaluate to True, and 
   the resulting boolean value will be returned and passed to the print()
   function. We will see 'True' printed in our console/notebook. 

```python
print(is_two(2))
```
```python
True
```
