from tabulate import tabulate


print("Hello, World")

student_name="Allen"
student_age=32
print("Student Name:", student_name)
print("Student Age:", student_age)

num1 = 15
num2 = 10
total=num1+num2
print("The sum is", total)



data = [
    ["Name: " "Allen"],
    ["Username: " "Allenumills"],
    ["Location: " "Liverpool"]
]

print(tabulate(data, tablefmt="outline"))