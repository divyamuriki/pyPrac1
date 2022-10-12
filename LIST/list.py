#Sum of elements:
'''list1=[1,2,3,4,5]
list2=[4,5,6,7]
list=list1+list2
print(list)
Sum = sum(list1)
print(Sum)
#Mulitply of elements
import numpy

list1 = [1, 2, 3]
list2 = [3, 2, 4]

# using numpy.prod() to get the multiplications
import numpy as np
list1 = [1, 2, 3]
list2 = [3, 2, 4,5,4]
result1 = np.prod(list1)
result2 = np.prod(list2)
result3 = np.mean(list1)
result4 = np.median(list2)
print(result1)
print(result2)
print(result3)
print(result4)
def multiplyList(myList):
    result = 1
    for i in myList:
        result = result * i
    return result
list1 = [1, 2, 3]
list2 = [3, 2, 4]
print(multiplyList(list1))
print(multiplyList(list2)
#3.Largest number from list
list1 = [1, 2, 3]
print(max(list1))
print(sum(list1))
#4.Smallest number from list
print(min(list1))
#5.Remove duplicates
mylist = ["a", "b", "a", "c", "c"]
mylist = list(dict.fromkeys(mylist))
print(mylist)
#6.Check list is empty or not
list1=['Geeks', 'Geeks', 'Geeks', 'Geeks' ]
if len(list1)==0:
    print("empty list")
else:
    print(" list")
list1 = ['Geeks', 'Geeks', 'Geeks', 'Geeks']
list2=[]
if list2:
    print("empty list")
else:
    print(" list")
#7Clone or copy
x = [1, 2, 3]
y= print(x.copy())
z=print(x)
#8.Find common element from 2 lists
list1 = [1,2,3,4,5,6]
list2 = [3, 5, 7, 9]
for i in list1:
    list2.append(i)
print(str(list2))
print(type(list2))
for i in list1:
    list2.extend(i)
print(list2)
print(list1.extend(list2))
list3=print(list1+list2)
print(list(set(list1).intersection(list2)))
print(list(set(list1).symmetric_difference(list2)))
#9.Remove specified index from list and print
list1 = [1,2,3,4,5,6]
list1.pop(2)
print(list1)
#10.Remove even elements and print list
list1 = [1,2,3,4,5,6]
for i in list1:
    if i%2!=0:
      print(i,end="")
#Shuffle list and print
import random
mylist = ["apple", "banana", "cherry"]
random.shuffle(mylist)
print(mylist)
#Difference betweeen 2 lists
li1 = [10, 15, 20, 25, 30, 35, 40]
li2 = [25, 40, 35]
li3=[]
for i in li1:
    if i not in li2:
        li3.append(i)
print(li3)
#To access index of list
listB = ['Sun','Mon','Tue','Wed','Thu','Fri','Sat']
print("Index of Wed: ",listB.index('Wed'))
print(listB[4])
#List of characters into string
listB = ['Sun','Mon','Tue','Wed','Thu','Fri','Sat']
print(str(listB))
#Finding index of an item in specified list
listB = ['Sun','Mon','Tue','Wed','Thu','Fri','Sat']
print(listB.index('Fri'))
#Flatten a shallow Append a list to second list
lst = [[10, 20, 30, 40], [50, 60, 70, 80], [90, 100, 110, 120]]
flatlist = []
for sublist in lst:
   for item in sublist:
      flatlist.append(item)
print (flatlist)
#Select an item randomly
import random
mylist = ["app", "bana", "cherr"]
random.choice(mylist)
print(mylist)
#Finding a second smallest number
lst = [10, 20, 30, 40,50, 60, 70, 80]
lst.sort()
print(lst[1])
#Finding a second largest number
lst = [10, 20, 30, 40,50, 60, 70, 80]
lst.sort(reverse=True)
print(lst[1])
#Get unique values
st1 = [10, 20, 30, 40,10]
print(set(st1))'''
#Frequency of elements
list1 = [10, 20, 30, 40,10,40,10]
count=0
for i in list1:
    if list1.count(i)>1:
        count=count+1
print(count)
# Counting number elementswithin a specified ranges
# Check a list contains sublist
# Generate all sublists
# Printing elements in ascending order
# Create a list by concatenating a given list which range goes from 1 to n
# Variable unique identification number
# Finding common items from two lists
# Change the position of every nth value with (n+1)th value
# Converting multiple integers into single integer
# Split a list based on first character of word
# Create multiple list
# Find missing and additional values
# Split a list into different variables
# Generate group of five consecutive numbers in a list
# Convert a pair of values into a sorted unique array
# Slect odd items of a list
# Insert an element before each element of a list
# Print a nested lists (each list on a new line) using the print() function
# Convert list to list of dictionaries
# Sort a list of nested dictionaries
# Split a list every Nth element
# Compute the similarity between two lists
# Create a list with infinite elements
# Concatenate elements of a list
# Remove key values pairs from a list of dictionaries
# Convert a string to a list
# Check if all items of a list is equal to a given string
# Replace the last element in a list with another list
# Check if the n-th element exists in a given list
# Find a tuple, the smallest second index value from a list of tuples
# Create a list of empty dictionaries
# Print a list of space-separated elements
# Insert a given string at the beginning of all items in a list
# Iterate over two lists simultaneously
# Access dictionary keys element by index
# Find the list in a list of lists whose sum of elements is the highest
# Find all the values in a list are greater than a specified number
# Extend a list without append
# Remove duplicates from a list of lists
# Get the depth of a dictionary
# Check if all dictionaries in a list are empty or not
# Two digits m (row) and n (column) as input and generates a two-dimensional array. The element value in the i-th row and j-th column of the array should be i*j
# A list contains group of strings.Convert each word to capital letter and print
# Reverse list of elements and print in upper case
# Write a Python program to convert month name to a number of days
# #Check circularly identical in two lists