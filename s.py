a = float(input("a number "))
x = math.sqrt(a)
y = round((a ** (1 / 3)), 4)
cube = False
square = False

if (x == round(x)):
    square = True

if (y == round(y)):
    cube = True

if cube == True and square == True:
    print(str(a) + " is both a perfect square and perfect cube.")
elif square == True:
    print(str(a) + " is only a perfect square.")
elif cube == True:
    print(str(a) + " is only a perfect cube.")