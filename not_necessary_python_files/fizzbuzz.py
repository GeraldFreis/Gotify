for i in range(0, 100):
    if i == 0:
        print(i)
    elif i % 3 == 0 and i % 5 is not 0:
        print(str(i) + " fizz")
    elif i % 5 == 0 and i % 3 is not 0:
        print(str(i)+ " buzz")
    elif (i % 3 ==0) and (i % 5 == 0):
        print(str(i) + " Fizzbuzz")
    else:
        print(i)
    i += 1