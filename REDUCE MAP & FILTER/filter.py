#normal function
l= [1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,12 ,13 ,55 ,767 ,7 ,78 ,888 ,99 ,755 ,34343 ,233]
def filter_fun(a):
    return a>100
newl=list(filter(filter_fun, l))
print(newl)

#lambda function
newl= list(filter(lambda a:a>100,l))
print(newl)