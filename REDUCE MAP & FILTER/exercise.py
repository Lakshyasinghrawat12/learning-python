#convert the names to upper case and print them in a list
name= ["lakshya", "aditya", "krishna", "prakhar", "ram", "sam", "ritik", "sonal"]

up_name= list(map(str.upper,name))
print(up_name)

#add 3 to all the numbers in list then filter out all numbers greter than 10
num=[0, 1, 33, 4, 5, 6, 7, 8, 9]

newnum= list(map(lambda x: x+3, num))
print(newnum)
new_num=list(filter(lambda x: x>10,newnum))
print(new_num)


#filter out all the marks greter than 70

stu_number=[100, 89, 80, 45, 90, 99, 78, 56, 77, 89, 88, 81]

filter_num= list(filter(lambda x: x>80, stu_number))
print(filter_num)


#filter out names of studen with markes over 20
dic={
    "lakshya": 100,
    "Krishna": 80,
    "Aditya": 99,
    "Prakhar": 89
}

new_dic= dict(filter(lambda item: item>90, dic))
print(new_dic)