#CS 161 week 5 assignments
#Alex Meador
#1
user_num = float(input("Enter a number: "))
if user_num % 5 == 0:
    print(f"{user_num} is divisible by 5")
else:
    print(f"{user_num} is not divisible by 5")
    
#2.1
    
state_capitals = {
    "Oregon": "Salem",
    "Washington": "Olympia",
    "Idaho": "Boise",
    "Wisconsin": "Madison",
    "Colorado": "Denver",
    "Florida": "Tallahasse"
}
state_name = input("Enter a state name: ")

if state_name == "Oregon":
    print(f"The capital of {state_name} is {state_capitals['Oregon']}.")
elif state_name == "Washington":
    print(f"The capital of {state_name} is {state_capitals['Washington']}.")
elif state_name == "Idaho":
    print(f"The capital of {state_name} is {state_capitals['Idaho']}.")
elif state_name == "Wisconsin":
    print(f"The capital of {state_name} is {state_capitals['Wisconsin']}.")
elif state_name == "Colorado":
    print(f"The capital of {state_name} is {state_capitals['Colorado']}.")
elif state_name == "Florida":
    print(f"The capital of {state_name} is {state_capitals['Florida']}.")
else:
    print("I do not know that one.")
    
#2.2

state_name = input("Enter a state name: ")
match state_name:
    case "Oregon":
       print(f"The capital of {state_name} is {state_capitals['Oregon']}.") 
    case "Washington":
       print(f"The capital of {state_name} is {state_capitals['Washington']}.")
    case "Idaho":
       print(f"The capital of {state_name} is {state_capitals['Idaho']}.")
    case "Wisconsin":
       print(f"The capital of {state_name} is {state_capitals['Wisconsin']}.")
    case "Colorado":
       print(f"The capital of {state_name} is {state_capitals['Colorado']}.")
    case "Florida":
       print(f"The capital of {state_name} is {state_capitals['Florida']}.")

#3.1

user_state = input("Enter a state name: ")
if user_state == 'Wisconsin':
    print('The capital of Wisconsin is Madison.')
elif user_state == 'Colorado':
    print('The capital of Colorado is Denver.')
elif user_state == 'Oregon':
    print('The capital of Oregon is Salem.')
elif user_state == 'Washington':
    print('The capital of Washington is Olympia.')
elif user_state == 'Idaho':
    print('The capital of Idaho is Boise.')
elif user_state == 'Florida':
    print('The capital of Florida is Tallahassee.')
else:
    print('I do not know that one.')
    
#3.2

state = {
    "Oregon": "Salem",
    "Washington": "Olympia",
    "Idaho": "Boise",
    "Wisconsin": "Madison",
    "Colorado": "Denver",
    "Florida": "Tallahasse"
}

capital = state.get("Oregon", "Not found")
print(capital)

#3.3

state = input("Enter a state name: ")
match state:
    case 'Wisconsin':
        print('The capital of Wisconsin is Madison.')
    case 'Colorado':
        print('The capital of Colorado is Denver.')
    case 'Oregon':
        print('The capital of Oregon is Salem.')
    case 'Washington':
        print('The capital of Washington is Olympia.')
    case 'Idaho':
        print('The capital of Idaho is Boise.')
    case 'Florida':
        print('The capital of Florida is Tallahassee.')
    case _:
        print('I do not know that one.')

#4

def entrance_fees(age):
    """Returns the entrance price based on age."""
    if age < 2:
        return 0
    elif age >= 2 and age < 11:
        return 3
    elif age >= 11 and age < 60:
        return 6
    else:
        return 4
age = int(input("Enter your age: "))
print(f"The entrance fee is: {entrance_fees(age)}")

#5

import requests

x = requests.get('http://coccbobcat.com/')
count = x.text.count('160')
print(print(f'The substring "160" appears {count} times in the HTML source of http://coccbobcat.com.'))

#6

import psutil

processes = len(psutil.pids())
print(f'Number of running processes: {processes}')



    
