first = float (input("Enter first number =>"))
sec = float (input("Enter second number =>"))
opr = input("Enter operation (+,-,*,/) =>")

result = eval(f"{first} {opr} {sec}")
print (result)