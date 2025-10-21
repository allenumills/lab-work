"""
This file contains the code from the Week 3 lab exercise,
Foucsing on for loops, While loops, and Github integrations.
"""
# For loop that prints numbers from 1 to 10
for i in range(10):
    print( i+1),

# for loop that prints even numbers from 0 to 20
for i in range(0, 21, 2):
    print(i)

# Using for loop to calculate the total espending
cost = [15.00 , 12.50 , 3.75, 40.25, 6,99]
total_cost = 0
for costes in cost:
    total_cost += costes
print(f"Total cost: $, {total_cost:.2f}")

# Exercise 3: Nassted for loops - pattern generation
for row in range(5):
    for column in range(5):
        print("*", end=" ")
    print()  # Move to the next line after each row

# step 2: create a right- angled triangle pattern
for row in range(1, 6):
    for column in range(row):
        print("*", end=" ")
    print()  # Move to the next line after each row

# Exercise 4: While loops - menu- driver calculator
while choice != 'Q':
    print("******Menu******")
    print("1. Add")
    print("2. Subtract")
    print("Q. Quit")
    choice = input("Please select an option: ")

    if choice == '1':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 + num2
        print(f"The result is: {result}")
    elif choice == '2':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 - num2
        print(f"The result is: {result}")