def test_feb(n):
    a=0
    b=1
    for i in range(n):
        yield a
        a=b
        b=a+b

for i in test_feb(10):
    print (i)