# """
# Iterable-an python object that has two methods (__iter__() or __getitem__()) defined within it that returns an iterator 
# Iterator- __next__()
# Iteration-
# String are by default iterable
# """
def gen(n):
    for i in range(n):
        yield i
g=gen(90)
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__iter__())



name="Lakshya"
nameir= iter(name)
print(nameir.__next__())
print(nameir.__next__())
print(nameir.__next__())
print(nameir.__next__())
print(nameir.__next__())
print(nameir.__next__())
print(nameir.__next__())