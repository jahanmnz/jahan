first = float (input("Enter first number =>"))
sec = float (input("Enter second number =>"))
opr = str(input("Enter operation (+,-,*,/) =>"))

result = eval(f"{first} {opr} {sec}")
print (result)