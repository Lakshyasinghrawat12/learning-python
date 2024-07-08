# normal application of map
def cube(x):
    return x*x*x

l= [1, 2, 3, 4, 5, 6]
newl=list(map(cube,l))
print(newl)

#lambda function
newl= list(map(lambda x:x*x*x,l))
print(newl)
