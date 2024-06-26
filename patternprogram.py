# 1
# 12
# 123
# 1234
# 12345
# n=int(input("enter the number"))
# for i in range(0,n):
#     for j in range(i+1):
#         print(j+1,end=" ")
#     print()

# 1
# 21
# 321
# 4321
# 54321
# n=int(input("enter the number"))
# for i in range(0,n):
#     for j in range(i,-1,-1):
#         print(j+1,end=" ")
#     print()

# 1
# 22
# 333
# 4444
# 55555
# n=int(input("enter the number"))
# for i in range(0,n):
#     for j in range(i+1):
#         print(i+1,end=" ")
#     print()

#55555
#4444
#333
#22
#1
# n=int(input("enter the number"))
# for i in range(0,n):
#     for j in range(i+1):
#         print(n-i,end=" ")
#     print()

# 5
# 54
# 543
# 5432
# 54321
# n=int(input("enter the number"))
# for i in range(0,n):
#     for j in range(i+1):
#         print(n-j,end=" ")
#     print()

# *
# **
# ***
# ****
# *****
# n=int(input("enter the number"))
# for i in range(0,n):
#     for j in range(i+1):
#         print('*',end=" ")
#     print()

# *****
# ****
# ***
# **
# *
# n=int(input("enter the number"))
# for i in range(0,n):
#     for j in range(i,n):
#         print('*',end=" ")
#     print()

#     *
#    **
#   ***
#  ****
# *****
# n=int(input("enter the number"))
# for i in range(0,n):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print('*',end=" ")
#     print()

# *****
#  ****
#   ***
#    **
#     *
n=int(input("enter the number"))
for i in range(0,n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n):
        print('*',end=" ")
    print()