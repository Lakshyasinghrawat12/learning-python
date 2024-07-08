##* lambda function are not defined by def keywork but by lambda key word
#* Retrun experssion but bot values
#* one line function
#* any number & argument
#* cannot access global varaibels
#* function does not have any name and can be assigned to a varaible

# syntax of lambda
#function_name= lambda variable: logic
# print(function_name(value))

# double= lambda x: x*2
# print(double(5))

# powerof= lambda a,b: a**b
# print(powerof(2,3))

#to convert celsius to feranhiet and visa versa
temp= int(input("Enter the temperature"))
unit= input("Enter the unit of temperature ")
if unit == "Celcius" or "C" or "c":
    toferan= lambda temp: ((temp*(1.8000))+ 32.00)
    print(toferan(temp))
elif unit == "Fahrenhiet" or "F" or "f":
    tocel= lambda temp: (temp-32)*(5/9)
    print(tocel(temp))
else:
    print("Wront input")
