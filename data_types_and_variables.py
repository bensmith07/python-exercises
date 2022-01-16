# Create a Python script file named 
# data_types_and_variables.py. Inside it, write some 
# Python code, that is, variables and operators, to 
# describe the following scenarios. Do not worry about the 
# real operations to get the values, the goal of these 
# exercises is to understand how real world conditions can 
# be represented with code.


# 1) You have rented some movies for your kids: 
# The little mermaid (for 3 days), Brother Bear 
# (for 5 days, they love it), and Hercules (1 day, 
# you don't know yet if they're going to like it). 
# If price for a movie per day is 3 dollars, how much 
# will you have to pay?

price_per_day = 3.00
days_rented_TheLittleMermaid = 3
days_rented_BrotherBear = 5
days_rented_Hercules = 1

total_price = (price_per_day 
              * days_rented_TheLittleMermaid 
              * days_rented_BrotherBear 
              * days_rented_Hercules)

print()
print('The total movie rental price is $', total_price)

# 2) Suppose you're working as a contractor for 3 companies: 
# Google, Amazon and Facebook, they pay you a different 
# rate per hour. Google pays 400 dollars per hour, 
# Amazon 380, and Facebook 350. How much will you receive 
# in payment for this week? You worked 10 hours for Facebook, 
# 6 hours for Google and 4 hours for Amazon.

hourly_rate_Google = 400.0
hourly_rate_Amazon = 380.0
hourly_rate_Facebook = 350.0

hours_worked_Google  = 6
hours_worked_Amazon = 4
hours_worked_Facebook = 10

total_pay = (hourly_rate_Google * hours_worked_Google
            + hourly_rate_Amazon * hours_worked_Amazon
            + hourly_rate_Facebook * hours_worked_Facebook)

print()
print('The total weekly pay is $', total_pay, '.')


# 3) A student can be enrolled to a class only if the class is 
# not full and the class schedule does not conflict with her 
# current schedule.

def enroll():
    pass

class_is_full = False
class_schedule_conflict = False

if class_is_full == False and class_schedule_conflict == False:
    enroll()
    print()
    print('Enrollment successful.')
else:
    print()
    print('Student may not enroll in this class.')


# 4)  A product offer can be applied only if people buys more than
# 2 items, and the offer has not expired. Premium members do
# not need to buy a specific amount of products.

def apply_offer():
    pass

min_items = 3

items_in_cart = 3
is_premium_member = False

if is_premium_member:
    apply_offer()
    print()
    print('Offer successfully applied.')
else:
    if items_in_cart >= min_items:
        apply_offer()
        print()
        print('Offer successfully applied.')
    else:
        print()
        print('Cannot apply offer. Must be more than 2 items.')


# 5)  Create a variable that holds a boolean value for each 
# of the following conditions:
# - the password must be at least 5 characters
# - the username must be no more than 20 characters
# - the password must not be the same as the username
# - bonus neither the username or password can start or 
#   end with whitespace

def create_account():
    pass

username = 'codeup'
password = 'notastrongpassword'

min_chars = 5
max_chars = 20

password_meets_min_chars = len(password) >= min_chars
username_meets_max_chars = len(username) <= max_chars
username_password_are_unique = username != password
username_password_no_whitespace = (username[0].isspace() == False \
                                  and username[-1].isspace() == False \
                                  and password[0].isspace() == False \
                                  and password[-1].isspace() == False)

if password_meets_min_chars \
and username_meets_max_chars \
and username_password_are_unique \
and username_password_no_whitespace:
    create_account()
    print()
    print('Account created.')
else:
    print()
    print('Invalid username/password combination.')

