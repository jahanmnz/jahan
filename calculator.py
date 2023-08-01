first = float(input("Enter first number =>"))
sec = float(input("Enter second number =>"))
opr =str(input("Enter operation (+,-,*,/) =>"))

if opr == "+":
    total = first + sec
elif opr == "-":
    total = first - sec
elif opr == "*":
    total = first * sec
elif opr == "/":
    total = first / sec
else:
    total=str("Gham daroo sayee operation select ko")
print (total)