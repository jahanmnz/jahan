"""thistuple=("apple","banana","mangoo","bgi khuda")
print((thistuple))""


x= ("apple","banana","watermelon")
y = list(x)
y[2]= "kiwi"
x= tuple(y)
print(x)"""


fruits = ("apple", "banana", "cherry","watermelon","mangoo")

(green, *yellow, red) = fruits

print(green)
print(yellow)
print(red)