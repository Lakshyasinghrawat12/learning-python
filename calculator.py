import math
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def percentage(x, y):
    return x / y * 100

def exponantial(x, y):
 return x ** y

def floor_devision(x, y):
    return x // y

print("Select the operation")
print("1 to perform addition")
print("2 to perform subtraction")
print("3 to perform multiplication")
print("4 for division")
print("5 for percentage")
print("6 for exponantial")
print("7 for floor division")

while True:
    choice=input("Enter your choice =")
    if choice in ('1','2','3','4','5','6','7'):
        num1=float(input("first number"))
        num2=float(input("second number"))

        if choice == '1':
            print(num1,'+',num2,'=',add(num1, num2))

        elif choice == '2':
            print(num1,'-',num2,'=',subtract(num1, num2))

        elif choice == '3':
            print(num1,'*',num2,'=',multiply(num1, num2))

        elif choice == '4':
            print(num1,'/',num2,'=',divide(num1, num2))

        elif choice == '5':
            print(num1,'/',num2,'*',100,'=',percentage(num1, num2))

        elif choice == '6':
            print(num1,'**',num2,'=',exponantial(num1, num2))
        
        elif choice == '7':
            print(num1,'//',num2,'=',floor_devision(num1, num2))

        continue_calculation=input("to continue calculation type yes: ")
        if continue_calculation == "no":
            break

    else:
        print("invalid input")