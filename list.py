# lst=[1,2,3,4,5,6,7]
# print(lst[1])


# lst=[1,2,3,"4",5.0,3j+5,False]
# print(lst[1])


# lst=[[1,2,3],["4",5.0],[3j+5,False]]
# print(lst[1][1])


# lst=[[1,2,3],["4",5.0,7],[3j+5,False,8]]
# print(type(lst[1][0]))


# lst=[[[1,2],[3,4],[5,7]],[5,6,7,8]]
# print(lst[1][0])


# lst=[1,2]
# lst.append(50)
# print(lst)


# lst=[1,2,3,4,5]
# lst.insert(5,6)
# print(lst)


# lst=[1,2,3,4,5,"praj"]
# lst.remove("praj")
# print(lst)


# lst=[1,2,3,4,5]
# lst2 =lst.copy()#Deep copy
# lst2.append(1)
# print(lst)
# print(lst2)


# lst=[1,2,3,4,5]
# lst2 =lst#shallow copy
# lst2.append(1)
# print(lst)
# print(lst2)


# lst1=[1,2]
# lst2=[3,4]
# lst1.extend(lst2)
# print(lst1)


# lst1=[1,2]
# lst2=[[3,4]]
# lst1.append(lst2)
# print(lst1)



# lst1=[1,2,3]
# lst1.clear()
# print(lst1)


# lst=[1,2,3,
# [4,5],
# [[1,2,3],
# [4,5,6],
# [7,8,9]],
# "hi"]
# print(lst[4])


# lst=[5,2,3,4,6,7,8,1]
# print(type(lst))
# print(lst[3:17:2])
# print(lst.sort())


# lst=[5,2,3,4,6,7,8,1]
# lst.sort()#prints in assending order
# print(lst)


# lst=[5,2,3,4,6,7,8,1]#reverse list
# lst.reverse()
# print(lst)


# lst=[5,2,3,4,6,7,8,1]
# lst.sort(reverse=True)
# print(lst)


# a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
# b=a[7]+a[4]
# print(b)

# abc={"ki":[1,2,3,4,5,{"1":"one"}]}
# # print(type(abc["ki"][6]["1"]))
# # print(type(abc))
# print(abc["ki"][5]["1"].isdigit())

# LST=[1,2,3,{"KI":[1,2,3,4,5],
# "K2":"sTRING"}]
# print(lst["k2"][3])

# lst=[1,2,3,4,5,6]
# print(lst.index(2))

#Python program to multiply two numbers using function

# def add_num(a,b):#function for multiplication
#     multiply=a*b
#     return multiply; #return value
# num1=int(input("input the number one: "))#input from user for num1
# num2=int(input("input the number one: "))#input from user for num2

# print("The product is",add_num(num1,num2))#call te function


lst=[]
for i in range(1):
    lst=list(input("enter elements in a list"))
    print(lst)