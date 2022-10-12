# Prints each item and its corresponding type from the following list.
datalist = [1452, 11.23, 1 + 2j, True, 'w3resource', (0, -1), [5, 12],
            {"class": 'V', "section": 'A'}]
for item in datalist:
    print("Type of ", item, " is ", type(item))

# Add a key to a dictionary
capitals ={'uk':'landon','france':'berlin'}
capitals['usa']='america'
print(capitals)
# Check if a given key already exists in a dictionary.
d={"key":10,"key":23}
if "key" in d:
    print("keys exists")
else:
    print("key does not exists")

# Merge two Python dictionaries
employees={1:'macheel',2:'eric',3:'michael'}
new_hires={4:'eric',1:'julia'}
employees.update(new_hires)
print(employees)

# Sum all the items in a dictionary
dict1={'python':90,'cpp':100,'java':80,'pgp':50}
sum=0
for i in dict1.values():
    sum=sum+i
print(sum)
# or
d={'python':20,'cpp':100,'java':20,'pgp':40}
print(sum(d.values()))

# Multiply all the items in a dictionary
d={'a':23,'b':45,'c':367,'d':687}
m_value=1
for i in d:
    m_value=m_value*d[i]
    print('multification value',m_value)
# how to reverse a dictionary in python
dictionary ={'sara':25,'james':90,'mike':34}
r_dictionary=dict()
for key,value in dictionary.items():
    r_dictionary[value]=key
print(r_dictionary)

# Get the maximum and minimum value in a dictionary.
my_dict={'x':500,'y':5874,'z':560}
print(max(my_dict.values()))


# Remove duplicates from Dictionary
dict1={'a':10,'b':20,'c':30,'d':40,'e':20}
dict2={}
for key,value in dict1.items():
    if value not in dict2.values():
        dict2[key]=value
print(dict2)


# Combine two dictionary adding values for common keys.
d1={'a':100,'b':200,'c':300}
d2={'a':200,'d':400,'e':300}
for key in d1:
    if key in d2:
        d2[key]=d1[key]+d2[key]
    else:
        d2[key]=d1[key]
print(d2)

# Create a dictionary from a string.
str1='t3so'
my_dict={}
for letter in str1:
    my_dict[letter]=my_dict.get(letter,0)+1
print(my_dict)



# Print a dictionary in table format.
data =[["one",1],
       ["two",2],
       ["three",3],
       ["four",4],
       ["five",5],
       ]
for row in data:
    spaces=(5-len(row[0]))*' '
    print(row[0],spaces,row[1])

# To get the key, value and item in a dictionary.
dict_num={1:10,2:20,3:30,4:40,5:50}
print("key value count")
for count,(key,value) in enumerate(dict_num.items(),1):
    print(key," ",value," ", count)

# print a dictionary line by line.
# student_list= {"bob":False,
#                "cherlin":True,
#                "debble":False
#                }
# for name in student_list:
#     if student_list[name]==True:
#         print(name)

cars={"A":{"speed":70,
           "color":2},
           "B":{"speed":60,
           "color":3}}
for keys, values in cars.items():
    print(keys)
    print(values)
# Check multiple keys exists in a dictionary.
d={1:10,2:20,3:30,4:40,5:50}
def is_key_present(x):
    if x in d:
        print("key is present in the dictionary")
    else:
        print("key is not presnet in the dictionary")

is_key_present(5)
is_key_present(6)
