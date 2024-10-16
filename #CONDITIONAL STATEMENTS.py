#CONDITIONAL STATEMENTS

#Syntax
# if(condition):
#     statement 1
# elif(condition):
#     statement 2
# else:
#     statement N

# light = input("enter thr light: ")

# if(light == "red"):
#     print("stop")
# elif(light == "green"):
#     print("go")
# elif(light == "yellow"):
#     print("look")

# marks = int(input("Enter marks : "))
# if(marks >= 90):
#     print("good grade A")
# elif(90 > marks >=80):
#     print("grade = B")
# elif(80 > marks >= 70):
#     print("grade = C")
# elif(70 > marks >= 60):
#     print("grade = D")

# age = int(input("Enter age of the person : "))
# if(age >=18):
#     if(age >= 80):
#         print("cannot drive")
#     else:
#         print("can drive & vote")
# else:
#     print("cannot drive & vote")

#QUESTIONS FOR PRACTICE

#Write a program to check if a number entered by the user is odd or even 

# num = int(input("Enter the number : "))
# if(num % 2==0):
#     print("number is even")
# else:
#     print("number is odd")

#Write a program to find the greatest of 3 numbers entered by the user

# num1 = int(input("enter first number : "))
# num2 = int(input("Enter second number : "))
# num3 = int(input("Enter third number : "))
# if(num1 > num2 and num1 > num3):
#     print("first number is greater")
# elif(num2 > num3):
#     print("second number is greater")
# else:
#     print("third number is greater")


# Write a program to check if a number is multiple of any num or not 

num = int(input("enter number : "))
number = int(input("enter any number :"))
if(num % number == 0):
    print("num is multiple of number")
else:
    print("not a miltiple")


# Write a program to check if number or word is  pallindrome or not
# var = (input("enter any number: "))

