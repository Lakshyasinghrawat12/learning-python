#normal function
from functools import reduce
num=[1 ,2 ,3 ,4 ,5]
def mysum(x,y):
    return x+y

sum= reduce(mysum, num)
print(sum)

#lambda function

from functools import reduce
num=[1 ,2 ,3 ,4 ,5]
sum= reduce(lambda x,y:x+y,num)
print(sum)