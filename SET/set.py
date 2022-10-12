# create a tuple.
x=("divya",1,"revanth",2)
print(x)
#create a tuple with different data types
x=("divya",1,"revanth",2,True)
print(x)
# create a tuple with numbers and print one item
x=(1,2,3,4,5)
print(x[2])
# unpack a tuple in several variables
x=(1,2,3)
a,b,c=(1,2,3)
print(a)
print(b)
print(c)
# add an item in a tuple.
x=(1,2,3)
x = x + (9,)
print(x)
x = x[:1] + (15, 20, 25) + x[:1]
# convert a tuple to a string
a=(1,2,3)
s=''
for i in a:
    s=s+str(i)
print(s)

# get the 4th element and 4th element from last of a tuple
# create the colon of a tuple
#  find the repeated items of a tuple
# check whether an element exists within a tuple
x=[2,4,6,7]
print(4 in x)
# convert a list to a tuple
x=[2,4,6,7]
print(tuple(x))
#  remove an item from a tuple
a=(2,4,5,9,5,10)
b=list(a)
print(b.pop(2))
print (tuple(b))
# slice a tuple
a=(2,4,5,9,5,10)
print(a[1:6])
# find the index of an item of a tuple.
a=(2,4,5,9,5,10)
print(a.index(5))
# find the length of a tuple
a=(2,4,5)
print(len(a))
# convert a tuple to a dictionary
[("akash", 10), ("gaurav", 12), ("anand", 14),
         ("suraj", 20), ("akhil", 25), ("ashish", 30)]
#  unzip a list of tuples into individual lists
#  a=(2,4)
x,y=(2,4,)
print(x)
print
# reverse a tuple.
a=(2,4,5)
b=list(a)
b.reverse()
print(tuple(b))
# convert a list of tuples into a dictionary

# print a tuple with string formatting
a=(1,2,3)
r=""
for i in a:
    r=r+str(i)
print(r)
#  replace last value of tuples in a list
a=(1,2,3,1)
print(a[1])
print(a.count(1))

#  to remove an empty tuple(s) from a list of tuples

# sort a tuple by its float element.

# Create a set.
a={1,2,3,4}
print(a)
# Iteration over sets.
a={1,2,3,4}
for i in a:
    a=a+1
print(1)
# Add member(s) in a set.
a={'1','2','3','4'}
b=a.add('5')
print(a)
# Remove item(s) from set
a={'1','2','3','4'}
b=a.remove('2')
print(a)
# Remove an item from a set if it is present in the set.
a={'1','2','3','4'}
print('3' in a)
b=a.discard('3')
print(a)
# Create an intersection of sets
a={'1','2','3','4'}
b={2,7,8,9,10}
y=a.intersection(b)
print
# Create a union of sets
a={'1','2','3','4'}
b={2,7,8,9,10}
y=a.union(b)
print
# Create set difference
a={'apple',"banana",2,4}
b={"banana",2,3}
y=a.difference(b)
print
# Create a symmetric difference.
a={'apple',"banana",2}
b={"banana",2,3}
y=a.symmetric_difference(b)
print
# Clear a set.
a={'apple',"banana",2}
print(a.clear())
# Find maximum and the minimum value in a set
a={'1','2','3','4'}
print(max(a))
# Find the length of a set
a={'1','2','3','4'}
print(len(a))
# Create an array of 5 integers and display the array items. Access individual element through indexes.
# Append a new item to the end of the array.
# Reverse the order of the items in the array.
# Append items from inerrable to the end of the array
# Convert an array to an array of machine values and return the bytes representation
# Append items from a specified list.
# Remove a specified item using the index from an array.
# Convert an array to an ordinary list with the same items.