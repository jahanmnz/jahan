"""def my_function(fnames):
    print("sadoo "+ fnames)

my_function("lawda ")
my_function("jindak ")
my_function("good boy ")""



def my_function(fnames,lastname):
    print("sadoo "+ fnames+lastname)

my_function("lawda ","asta")
my_function("jindak " ,"100%")""




def celsius_to_fahrenheit(celsius):
    print((celsius * 9/5)+32)

celsius = 25
function = celsius_to_fahrenheit(celsius)""



def print_triangle(n):
 for i in range (1, 6):
  print("*" * i)

print_triangle(5)



def is_vowel(char):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    if char in vowels:
        return True
    else:
        return False

characters = ['a', 'b', 'E', 'Z']
for char in characters:
    if is_vowel(char):
        print(f"{char} is a vowel.")
    else:
        print(f"{char} is not a vowel.")

 

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5))"""

 
factorial = float(input("Put factorail number=>"))
print(float( n *factorial("n" - 1)))