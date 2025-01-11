#CS 161 week 1 Homework
#Alex Meador
#1
pet_type = "dog"
pet_name = "Gibson"
print(f"I have a {pet_type} and his name is {pet_name}.")

#2

first_name = input("Enter your first name: ")
current_age = input("Enter your current age: ")
yearly_savings = input("Enter your yearly savings: ")
print(f"Hello {first_name}! You are currently {current_age} years old. In 10 years, you will be 30 years old. If you save $1200 each year, in 5 years you will have saved $6000. Your average monthly savings is $100.00.")

#3

seconds_in_january = 31*24*60*60
print(f"The number of seconds in January is {seconds_in_january}.")

#4

num_eggs = int(input("Enter the number of eggs: "))
quoteint = num_eggs // 12
remainder = num_eggs % 12
print(f"This makes {quoteint} dozen eggs with {remainder} left over.")
