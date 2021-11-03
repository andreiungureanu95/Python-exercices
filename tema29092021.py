#*****print max and minim from the list
lst=[55, 6, 777, 54, 6, 76, 101, 1, 6, 2, 6]
print("Minimul este:", max(lst))
print("Maximul este:", min(lst))

#*****count how many times 6 occur in the list.
lst=[55, 6, 777, 54, 6, 76, 101, 1, 6, 2, 6]
print(lst.count(6))

#*****Using .remove() method, clear the last element of the list.
#lst=[55, 6, 777, 54, 6, 76, 101, 1, 6, 2, 6]
lst=[55, 6, 777, 54, 6, 76, 101, 1, 6, 2, 6]
lst=lst[::-1]
lst.remove(6)
lst=lst[::-1]
print(lst)

#*****Concatenate two lists in the following order
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
list1.extend(list2)
print(list1)

#*****add the sub-list: ["socks", "tshirt", "pajamas"] to the end of the gift_list #gift_list=['socks', '4K drone', 'wine', 'jam']
gift_list=['socks', '4K drone', 'wine', 'jam']
sub_list=["socks", "tshirt", "pajamas"]
gift_list.append(sub_list)
print(gift_list)

# #*****Given 2D array calculate the sum of diagonal elements.
# #Ex: [[1,3,5],[1,4,6],[7,6,9]
matrice = [[1,3,5],[1,4,6],[7,6,9]]
suma = matrice[0][0] +matrice[1][1] + matrice[2][2]
print(suma)


#*****Add item 7000 after 6000 in the following Python List
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)

#*****Given a Python list, find value 20 in the list, and if it is present, replace it with 200.Only update the first occurrence of a value
list1 = [5, 10, 15, 20, 25, 50, 20]
index = list1.index(20)
list1[index] = 200
print(list1)

#*****Remove empty strings from the list of strings ["Mike", "", "Emma", "Kelly", "", "Brad"]
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
reset_list = list(filter(None, list1))
print(reset_list)


###*****Write a Python script to add a key to a dictionary.
dictionary = {"ana":10, "ion":20}
dictionary.update({"vasile":4})
print(dictionary)

dict={"name": "Plato", "country": "Ancient Greece", "born": -427, "teacher": "Socrates", "student": "Aristotle"}
#*****Print When was Plato born?
print(dict["born"])

#*****Change Plato's birth year from B.C. 427 to B.C. 428.
dict.update({"born":-428})
print(dict)

#*****Add 2 to the son's height.
dict = {"son's name": "Lucas", "son's eyes": "green", "son's height": 32, "son's weight": 25}
dict["son's height"] = dict["son's height"] + 2
print(dict)

#*****Using .get() method print the value of "son's eyes".
print(dict.get("son's eyes"))

#*****clear the dictionary here then print it.
dict.clear()
print(dict)