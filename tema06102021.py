# 1.Take two int values from user and print greatest among them
a = int(input("The first number:"))
b = int(input("The second number:"))
if a > b:
    print("a is the greatest")
elif b > a:
    print("b is the greatest")
else:
    print("the numbers are equals")

#sau
print(max(a,b))

# 2.A school has following rules for grading system:
# a. Below 25 - F
# b. 25 to 45 - E
# c. 45 to 50 - D
# d. 50 to 60 - C
# e. 60 to 80 - B
# f. Above 80 - A
# Ask user to enter mark and print the corresponding grade.
mark = float(input("The mark is :"))
if mark < 25:
    print("F")
elif mark in range(25, 45):
    print("E")
elif mark in range(45, 50):
    print("D")
elif mark in range(50, 60):
    print("C")
elif mark in range(60, 80):
    print("B")
else:
    print("A")

# 3.A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
# Ask user for quantity
price = int(input("quantity is:"))
if price > 1000:
    price = price - 0.1 * price
print("Total price is", price)

# 4.Write an if statement that asks for the user's name via input() function. If the name is "Bond" make it print
# "Welcome on board 007." Otherwise make it print "Good morning NAME". (Replace Name with user's name)

name = input("Your name is :")
if name == "Bond":
    print("Welcome on board 007.")
else:
    print(f"Good morning {name}")

# 5.Write a Python program to check the validity of password input by users.
# Validation :
# At least 1 letter between [a-z] and 1 letter between [A-Z].
# At least 1 number between [0-9].
# At least 1 character from [$#@].
# Minimum length 6 characters.
# Maximum length 16 characters.
passwd = input("Password is:")
specialSym = ['$', '@', '#']
if len(passwd) < 6:
    print('length should be at least 6')
if len(passwd) > 20:
    print('length should be not be greater than 8')
if not any(char.isdigit() for char in passwd):
    print('Password should have at least one numeral')
if not any(char.isupper() for char in passwd):
    print('Password should have at least one uppercase letter')
if not any(char.islower() for char in passwd):
    print('Password should have at least one lowercase letter')
if not any(char in specialSym for char in passwd):
    print('Password should have at least one of the symbols $@#')

# 6.Write a Python program that tells a user that the number they entered is not a 5 or a 6.
number = int(input("Number is"))
if number != 5 or number != 6:
    print("your number is ok")

# 7.Write an algorithm to print from 1 to 10
for i in range(1, 11):
    print(i)

# 8.print all multiples of 5 between 1 and 100 (including both 1 and 100).
for i in range(1, 101):
    if i % 5 == 0:
        print(i)
# sau
for i in range(0, 101, 5):
    print(i)

# 9.read three numbers and writes them all in sorted order.
nr1 = float(input("The first number is"))
nr2 = float(input("The second number is"))
nr3 = float(input("The third number is"))
list1 = [nr1, nr2, nr3]
list1.sort()
print(list1)

# 10.We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23. We are in trouble if the parrot is talking and the hour is before 7 or after 20.
# Return true if we are in trouble.
hour = int(input("Current hour is"))
print(hour <= 7 or hour >= 20)

# 11.Given a string, return a new string where "not " has been added to the front.
# However, if the string already begins with "not", return the string unchanged.
word = input("The word is")
if len(word) >= 3:
    if word[0:3] == "not":
        print(word)
    else:
        print("not" + word)
else:
    print("not" + word)

# 12.Given a string, return true if the string starts with "hi" and false otherwise.
word = input("The word is")
if len(word) >= 2:
    print(word[0:2] == "hi")
else:
    print("false")
# sau
word = input("The word is")
print(word.startswith("hi"))

# 13.Given 2 ints, a and b, return their sum. However, sums in the range 10..19 inclusive, are forbidden, so in that case just return 20.
number1 = int(input("First number is"))
number2 = int(input("Second number is"))
sum1 = number1 + number2
if sum1 in range(10, 20):
    sum1 = 20
print("Suma este ", sum1)

# 14. return the number of 9's in a list
# [1, 2, 9] → 1
# [1, 9, 9 ]→ 2
# [1, 9, 9, 3, 9] → 3
list2 = [1, 2, 3, 9]
print(list2.count(9))

# 15.We'll say a number is special if it is a multiple of 11 or if it is one more than a multiple of 11.
# Return true if the given non-negative number is special.
number3 = int(input("Number is"))
if number3 % 11 == 0 or (number-1) % 11 == 0:
    print("number is special")

# 16.Modify and return the given dictionary as follows: if the key "a" has a value, set the key "b" to have that same value. In all cases remove the key "c",
# leaving the rest of the dictionary unchanged.
# {"b": "bbb", "c": "ccc", "a": "aaa"} → {"b": "aaa", "a": "aaa"}
# {"b": "xyz", "c": "ccc"} → {"b": "xyz"}
# {"d": "hi", "c": "meh", "a": "aaa"} → {"d": "hi", "b": "aaa", "a": "aaa"}
dict2 = {"b": "bbb", "c": "ccc", "a": "aaa"}
if "a" in dict2.keys():
    dict2["b"] = dict2["a"]
print(dict2)
del dict2["c"]
print(dict2)

# 17 Given a dictionary of food keys and topping values, modify and return the dictionary as follows: if the key "potato" has a value, set that as the value for the key "fries". If the key "salad" has a value, set that as the value for the key "spinach".
#
# {"potato": "ketchup"} → {"fries": "ketchup", "potato": "ketchup"}
# {"potato": "butter"} → {"fries": "butter", "potato": "butter"}
# {"salad": "oil", "potato": "ketchup"} → {"salad": "oil", "fries": "ketchup", "spinach": "oil", "potato": "ketchup"}
dict3 = {"salad": "oil", "potato": "ketchup"}
if "potato" in dict3.keys():
    dict3["fries"] = dict3["potato"]
if "salad" in dict3.keys():
    dict3["spinach"] = dict3["salad"]
print(dict3)
# 18.Print n asterisks
n = int(input("n is:"))
print("*"*n)

# 19. Write a Python program to find those numbers which are divisible by 7 and multiple of 5,
#  between 1500 and 2700 (both included).
for i in range(1500, 2701):
    if i % 7 == 0 and i % 5 == 0:
        print(i)

# 20. Write a Python program to count the number of even and odd numbers from a series of numbers.
#  Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# Expected Output :
# Number of even numbers : 5
# Number of odd numbers : 4
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
even_numbers = 0
odd_numbers = 0
for i in numbers:
    if i % 2 != 0:
        even_numbers = even_numbers + 1
    else:
        odd_numbers = odd_numbers +1


# 21. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6
for i in range(7):
    if i != 3 or i != 6:
        print(i)

# 22. Print sum of the numbers between 20 and 100;
sum2 = 0
for i in range(20, 100):
    sum2 = sum2+i
print("Sum is : ", sum2)

# sau
print("Sum is : ", sum(list(range(20, 100))))