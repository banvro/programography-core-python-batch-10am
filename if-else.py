
# a = "10"

# b = int(a)

# print(a + b)

# Condational Statments

# syntax

# if condation:
    # indentation
    # block of code...



# age calculator


# age = int(input("Enter your age : "))

# if age > 18:
#     print("You are eligible for voat.")

# else:
    # only exectute if the condation is false



# age = int(input("Enter your age : "))

# if age > 18:
#     print("You are eligible for voat.")

# else:
#     print("you are not eligible for voat")


# elif ---> use when we have multiple condations




# age = int(input("Enter your age : "))

# if age > 18:
#     print("you ae eligible for voat")
    
# elif age == 18:
#     print("welcome! this is your first voat.")

# elif age == 19:
#     print("this is your secnd voat..!")

# else:
#     print("you are not eligible for voat")





# calculator

#  :::::::: My Calculator :::::::::

# enter first number : 10
# enter second number : 20
    
# Your options are :::::
#     1) Adation
#     2) Subtration
#     3) Multiplicion
#     4) Division
#     5) Exponent
#     6) Modulus
    
# Enter your choice : 1


# Programography


# print("::::::::: My Calculator ::::::::::::")

# print()
# num1 = int(input("Enter first number : "))
# num2 = int(input("Enter second number : "))

# print()

# print(''' Your options are : 
#         1) Adation
#         2) Subtraction
#         3) Mutiplication
#         4) Devsion
#     ''')

# choice = input("ENter your Choice : ")

# if choice == "1":
#     print(f"The sum of {num1} and {num2} is : {num1 + num2}")

# elif choice == "2":
#     print(f"The subtraction of {num1} and {num2} is : {num1 - num2}")

# elif choice == "3":
#     print(f"The multiplication of {num1} and {num2} is : {num1 * num2}")

# elif choice == "4":
#     print(f"The divsio of {num1} and {num2} is : {num1 / num2}")
    
# else:
#     print("Enter valid option..")
    


# Nested if else

# age = int(input("Enter first nunmber : "))

# if age > 18:
#     if age == 19:
#         print("You are elgible for voat..!")
#     print("doneeeeeeee")
    
# else:
#     print("not eligible")


# print("heloooooooooo")



# x = ?"this is car"

# y = ?car


x = " this is a car"[::-1]

zx = ""
k = ""
h = 0

print(x)

for i in x:
    if i == " ":
        zx = zx[::-1]
        k = k + zx + " "
        h = 0
        zx = ""
    
    else:
        h = h + 1
        zx = zx + i
        
print(zx)
print(k)






















