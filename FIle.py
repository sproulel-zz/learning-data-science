def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print('zero division error')
        return 0

x = float(input('First number to divide with: '))
y = float(input('number to divide by: '))
total = divide(x,y)
print('Answer: ', total)
