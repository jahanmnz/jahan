first = float (input("Enter first number =>"))
sec = float (input("Enter second number =>"))
opr = str(input("Enter operation (+,-,*,/) =>"))


if opr == "+":
    total = first + sec
elif opr == "-":
    total = first - sec
elif opr == "*":
    total = first * sec
elif opr == "/":
    total = first / sec
else:
    total=str("Select valid operation")

print (("Your anwser is ") + str (total))



