#1.Display the sum of 5 + 10, using two variables: x and y.
x = 5
y = 10
print(f'Suma numerelor {x} si {y} este ', x+y)

#2. Creați cȃte o variabilă de tipul: string, int și float, după cum urmează:
# Variabila de tip int va reține valoarea 20.
# Variabila de tip float va reține valoarea 10.
# Variabila de tip string reține valoarea “python”.
x_int = 20
y_float = 10.0
z_string = "python"

#3. Utilizȃnd funcția type, determinați tipul următoarelor variabile:
restanta = 0
notaFinala = 10.0
laborator = "Introducere in informatica"
print(type(restanta))
print(type(notaFinala))
print(type(laborator))

# # 4.Verificaţi dacă un cuvânt este palindrom. Un cuvânt este palindrom dacă scris de la dreapta la
# #stanga, este tot acel cuvânt.(folositi assert pt verificare)
palindrom = input ("Stringul pe care doresti sa il verificam este:")
assert palindrom == palindrom[::-1]

print("5. Remove first n characters from beginning of a string (n il cititi de la tatatura)")
text = input("Stringul este:")
n = int(input("Numarul este:"))
print("Noul string este ", text[n::])

print("5.reads two numbers and multiplies them together and print out their product")
x = int(input("Primul numar este:"))
y = int(input("Al doilea numar este:"))
print(f"Produsul numerelor {x} si {y} este:", x*y)

print("6.Check if the first and last character of a string  is the same stringul il cititi de la tastatura")
text = input("Stringul este:")
assert text[0] == text[len(text)-1]

print("7. Write a program to find how many times substring “Emma” appears in the given string.")
str_x = "Emma is good developer. Emma is a writer"
sub_str = "Emma"
x = str_x.count(sub_str)
print(f'{sub_str} is found in {str_x} for  {x} times')

print("8. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.")
# pt "eu merg la mare" sa imi afiseze "eure"
str_x = "eu merg la mare"
print("Stringul format din rimele 2 si ultimele 2 caractere este:", str_x[0:2]+str_x[(len(str_x)-3)::])
print("9. Write a Python program to calculate the length of a string.")
 # pt "eu merg la mare" ->15")
print(f"Lungimea sirului {str_x} este:", len(str_x))
print(" 10. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself. Go to the editor")
# Sample String : 'restart'
# Expected Result : 'resta$t'
str_x = "restart"
count = str_x.count("r")
reverse = str_x[::-1]
reverse = reverse.replace("r", "$",count-1)
str_x = reverse[::-1]
print(str_x)
# 11. Utilizand tipurile de print pe care vi le-am aratat:
# afisati in consola ""I have 1000 dollars so I can buy 3 football for 450.00 dollars.""
totalMoney = 1000
quantity = 3
price = 450
print("I have 1000 dollars so I can buy 3 football for 450.00 dollars.")
print(f'I have {totalMoney} dollars so I can buy {quantity} football for {price} dollars.')
print('I have {} dollars so I can buy {} football for {} dollars.'.format(totalMoney, quantity, price))
print('I have {} dollars so I can buy {} football for {} dollars.'.format(totalMoney, 9, price))

# 12.Build a program to calculate the followings using the input from the user for a, b, c or r
# • rectangle area and perimeter
length = float(input("Length is:"))
width = float(input("Width is:"))
print("Area is:", length*width)
print("Perimeter is", (2*length)+(2*width))
# • circle area
r = float(input("Raza cercului este:"))
PI = 3.14
aria_cercului = PI*(r**2)
print("Circle area is:", aria_cercului)

# 13. Which of the following are valid ways to specify the string literal foo'bar in Python:
# #gresit print('foo\'bar')
#  print("""foo'bar""")
#  print("foo'bar")
#  print('foo''bar')
# gresit print('foo'bar')

# 14.Password checker script
# Define a username getting input from the console
# Define a password getting input from the console
# Display the following message ‘The password for user Paul is
# ********* is 9 characters long)
username = input("Username is:")
password = input("Password is:")
length = len(password)
hide_password = "*"*length
print(f'The password for the user {username} is {hide_password} and is {length} characters long')

# de cautat pe net:
print("15.Write a program to take three names as input from a user in the single input() function call.")
a,b,c = input("Names are:").split()
print(a)
print(b)
print(c)
print("16. Display float number with 2 decimal places using print() pt num = 458.541315 afisati 458.54")
num = 458.541315
print(round(num,2))