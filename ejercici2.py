a = [4, 7, 9, 2, 67, 15, 624]
x= None
for elemento in a:
    if (x == None or elemento > x):
        x = elemento
print(x)