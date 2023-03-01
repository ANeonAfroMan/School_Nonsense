tasks = str(input("here: "))
num1 = ""
num2 = ""
num3 = ""
num4 = ""
count = 1
Total = 0
for x in tasks:
    if x.isnumeric():
        if count == 1: num1 = num1+x
        if count == 2: num2 = num2+x
        if count == 3: num3 = num3+x
        if count == 4: num4 = num4+x
    elif x != " ":
        count += 1
    else:
        count = 1
        num1 = int(num1)
        num2 = int(num2)
        num3 = int(num3)
        num4 = int(num4)
        if not(num1 > num4 or num3 > num2):
            Total+=1
        num1 = ""
        num2 = ""
        num3 = ""
        num4 = ""
print(Total)