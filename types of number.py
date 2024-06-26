#to check prime number
# num=int(input("enter a number"))
# for i in range(2,num):
#     if (num % i)==0:
#         print("number is not prime")
#         break
#     else:
#         print("number is prime")
#         break

#Python Program to Print the Fibonacci sequence
# num=int(input("enter number greater than zero:"))
# n1,n2=0,1
# sum=0
# if(num<=0):
#     print("enter number greater than zero")
# else:
#     for i in range(0,num):
#         print(sum)
#         n1=n2
#         n2=sum
#         sum=n1+n2

#Python Program to Print the amstrong number
# num=int(input("enter any four digit number"))
# original_num=num
# sum=0
# n=len(str(num))
# while num>0:
#     digit=num%10
#     sum=sum +digit**n
#     num=num//10
# if sum==original_num:
#     print("number is amstron")
# else:
#     print("number is not amstron")

#print 100 odd numbers

    # for i in range(200):
    # if i%2!=0:
    #     print(i)

# n=200
# while(n!=0):
#     if(n%2!=0):
#         print(n)
#     n=n-1


#print first 100 prime numbers
n=200
for number in range(2,n):
    if number>1:
        for i in range(2,number):
            if (number%i)==0:
                break
        else:
            print(number)

# a=0
# while(a<=200):
#     i=1
#     count=0
#     while(i<=200):
#         if(a%i==0):
#             count=count+1
#         i=i+1
#     if(count==2):
#         print(a)
#     a=a+1