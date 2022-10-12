'''# #1Length of string
# name="divyareddy"
# length=len(name)
# print(f'length of the name{length}')
# #2.Count characters in string
# name="divyarevanth"
# count=len(name)
# print(f"count of characters in name{count}")
# #3.String slicing
# str="vagalla divya reddy"
# print(str[0:7])
# 4.Length of longest string in python
str = input("enter string name")
sp = str.split()
max = 0
for i in sp:
    if len(i) > max:
        max = len(i)
        result=i
print(f"largest string is {result}")
# 5.First last chars swapping
str = input("enter string name")
sp=str.split()
sp[0],sp[-1]=sp[-1],sp[0]
print(sp)

name = 'shiva welcome'
print(name[-1]+name[1:-1]+name[0])

# 6.Remove odd index values
name = input("enter string name")
for i in range(len(name)):
    result = " "
    if i%2==0:
        result= result+name[i]
    print(result,end='')
# 7.Count words in a string
msg = "hey hi gud morining banglore"
print(len(msg.split()))

msg = "hey hi gud morining banglore"
print(len(msg))

msg = "hey hi gud morining banglore"
print(msg.count('g'))
 #8.Upper lower case of a string
msg = "hey hi gud morining banglore"
print(msg.upper())
print(msg.lower())
#9.last part of the string
name="revanth reddy"
print(name[-1])
name="revanth reddy divya"
part=name.split()
print(part[-1])
#10.Convert a given string to all uppercase
 upstr="hello python"
 print(upstr.upper())
# 11.program to remove a newline in Python
upstr = "hello  python\n"
print(upstr.strip())
# 12.program to check whether a string starts with specified characters
upstr = "hello python"
print(upstr.startswith('h'))
# 13.to set the indentation of the first line


# 14.to print the following floating numbers upto 2 decimal places
x=1344.2345
print(round(x,2))
#15.print the following floating numbers upto 2 decimal places with a sign
x=-1344.2345
y=round(x,2)
z=abs👍
print(z)

set={1,2,3,4}
list=['a','b','c','d']
list.update(set)
print(list)
# 16.to count occurrences of a substring in a string
greet="hello divya hello revanth hi shiva hi kumari"
sp=greet.split()
print(len(sp))'''

# 17.to display a number with a comma separator
a='12345'
print(list(a))
list=[9,8,7,6]
print(' '.join[str(list)])
# 18.count repeated characters in a string
name="hi hello how are you"
# 19.to format a number with a percentage

# 20.print the index of the character in a string
# 21.convert a string in a list
# 22.swap comma and dot in a string
# 23.count and display the vowels of a given text
# 24.remove spaces from a given string
# 25.move spaces to the front of a given string
# 26.capitalize first and last letters of each word of a given string
# 27.remove leading zeros from an IP address
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
list3=zip(list1,list2)