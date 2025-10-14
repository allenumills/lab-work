"""
This program calculates the area of a rectangle and prints the result.
"""

#Exercise 1: Python Syntax & Comments

current_degree=25
#This formula convert the Celsius to Fahrenheit
fahrenheit = (current_degree*9/5)+32
print(f"The weather is= {fahrenheit} Fahrenheit also it is={current_degree} Celsius")


#Exercise 2: Data Types & Variables

name="Allen "
age= 32
hight=180.1
studnet=True

print(f"Name is={name} and type of date is= {type(name)} ")
print(f"Age is={age} and type of date is= {type(age)} ")
print(f"Hight is={hight} and type of date is= {type(hight)} ")
print(f"Studnet is={studnet} and type of date is= {type(studnet)} ")


"""Python's flexibility with variable types stems from its dynamically-typed nature, which is a core feature of the language. Here's why Python allows you to change a variable's type later:

Dynamic Typing:
Python doesn't require you to declare a variable's type when you create it. Instead, the type is determined at runtime based on the value assigned to the variable. This means you can reassign a variable to a value of a different type, and Python will automatically update its type.

Example:

Python

Copy code
x = 42       # x is an integer
x = "hello"  # x is now a string
Ease of Use and Flexibility:
This feature makes Python highly flexible and beginner-friendly. Developers can focus on solving problems without worrying about strict type declarations, making the code concise and adaptable.

Rapid Prototyping:
Dynamic typing is particularly useful for quick experimentation and prototyping. You can easily test different approaches without being constrained by rigid type systems.

Underlying Implementation:
Python variables are essentially references to objects in memory. When you assign a new value to a variable, you're simply pointing it to a new object, regardless of its type.

While this flexibility is powerful, it can sometimes lead to bugs or confusion in larger projects. To mitigate this, Python introduced type hints in recent versions, allowing developers to optionally specify variable types for better readability and debugging.
"""

#Exercise 3: String Formatting

name1 = "Allen "
course ="Robotics & Artificial Intelligence "
favourite_programming_language = "Python "
favourite_movie = "Green Book "
c = name1 + course + favourite_programming_language + favourite_movie

print(f"Hello that is intersting thing about me {c} I'will tell you what is the type of data that i use to create that sentance. that is the type of date i use to write this print statment{type(name1)} {type(course)} {type(favourite_programming_language)} {type(favourite_movie)}")


#Exercise 4: Decision Making (if / elif / else)


while True:
    user_input = input("Enter your age: ")
    try:
        # Try to convert the input to an integer
        number = int(user_input)
        if number >= 18:
            print("You are an adult.")
        elif number == 17:
            print("Don't worry, next year you will be an adult.")
        else:
            print("You are a child.")
        break  # Exit the loop after valid input and response
    except ValueError:
        # If conversion fails, prompt the user again
        print("Invalid input. Please enter a valid number.")
