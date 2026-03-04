# # # # # def my_function():
# # # # #     print("Hello, World!")
# # # # # my_function()
# # # # # my_function()
# # # # def my_function(name):
# # # #     print(f"my name is :{name}")
# # # # my_function("Alice")
# # # # my_function("Bob")
# # # def my_function(first_name, last_name):
# # #     print(f"my name is :{first_name} {last_name}")
# # #     x = input("Enter your first_name: ")
# # #     y = input("Enter your last_name: ")
# # #     my_function(x, y)

# # # def my_function(first_name, last_name):
# # #     print(f"my name is :{first_name} {last_name}")
# # # x = input("Enter your first_name: ")
# # # y = input("Enter your last_name: ")
# # # my_function(x, y)
# # def my_registration(name, email, password = ""):
# #     print(f"Name: {name}")
# #     print(f"Email: {email}")
# #     print(f"Password: {password}")
# # name = input("Enter your name: ")
# # email = input("Enter your email: ")
# # password = input("Enter your password: ")
# # my_registration(name, email, password)
# def calculate_area(radius):
#     pi = 3.14159
#     area = pi * radius ** 2
#     return area
# radius = float(input("Enter the radius of the circle: "))
# area = calculate_area(radius)
# print(f"The area of the circle with radius {radius} is: {area}")
def cal (a,sign, b):
    if sign == "+":
        result = a + b
    elif sign == "-":
        result = a - b
    elif sign == "*":
        result = a * b
    elif sign == "/":
        result = a / b

    return result
num1 = float(input("Enter first number: "))
sign = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))
result = cal(num1,sign, num2)
# print(f"The sum of {num1} and {num2} is: {result}")
print(result)






