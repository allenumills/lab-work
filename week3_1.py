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