def fibonacci():
    x, y = 0, 1
    while True:
        yield x
        x, y = y, x + y

n = int(input("Input the number of Fibonacci numbers you want to generate? "))

print("Number of first ",n,"Fibonacci numbers:")
fib = fibonacci()
for _ in range(n):
    print(next(fib),end="\n")



# febinaci series
def test_feb(n):
    a=0
    b=1
    for i in range(n):
        yield a
        a=b
        b=a+b

for i in test_feb(10):
    print (i)