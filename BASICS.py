#BASICS OF PYTHON PROGRAMMING: https://www.youtube.com/watch?v=N4mEzFDjqtA

import random
import sys
import os

#Comment

''' 
Multiline Comment
'''

#single quotes or double quotes can be used to print a string
print('Hello World!')
print("Hello World!")

#Numbers, Strings, Lists, Tuples, Dictionaries

#** (two multiple stars is exponents)
#// (two slashes are used to divide but gives out integer values back as rounded down)

#automatically provides space after string if comma is used
print("3 * 2 =", 3 * 2)

quote = "\"Quote within a quote\""
multi_line_quote = '''Multiline quote'''

print(quote + " " + multi_line_quote)
#again, the commas provide spaces automatically between strings
print("%s %s %s" % ("this is how you add lines", quote, multi_line_quote))

print("I don't like ", end="")
print("newlines")

print("\n" * 3)

grocery_list = ['Juice', 'Tomatoes', 'Potato',
                'Bananas']
print(grocery_list[0])

grocery_list[0] = "poop"
print(grocery_list[0])

#print from index zero up to three (discluding three, thus prints index two)
print(grocery_list[0:3])

#list within a list
other_events = ["wash clothes", "pick up kids", "cash check"]
to_do_list = [grocery_list, other_events]
print(to_do_list)

#[0] means in first list which is grocery_list, you want index 1
#otherwise you can do [1] meaning second list which is other_events, you want index 1
print((to_do_list[1][1]))

#add onions in the list of grocery_list using append keyword
grocery_list.append("Onions")
print(grocery_list)

#insert an item in the list at a specific index
grocery_list.insert(1, "Pickles")
print(grocery_list)

#remove an item in the list
grocery_list.remove("Pickles")
print(grocery_list)

#sorts items alphabetically (capital letters first)
grocery_list.sort()
print(grocery_list)

#reverses the list of items in list
grocery_list.reverse()
print(grocery_list)

#another way of removing an item at index 4
del grocery_list[4]
print(grocery_list)

#combine the two lists together like you would normally with other variables
more_list = grocery_list + other_events
print("More list is:", more_list)

#get the length of a list
print(len(more_list))

#maximum (index 0)
print(max(grocery_list))

#minimum prints out n (index 0, 1, 2 , ... , n)
print(min(grocery_list))