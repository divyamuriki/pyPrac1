# excel sheet program
""" 1. Length of string """

# user_inp1 = input("what is your string : ")
# l1 = len(user_inp1)
# if l1 == 1 :
#     print("length of a string is : ",l1 , "charecter")
# else :
#     print("length of a string is : ", l1, "charectors")

""" 2. Count characters in string """

# user_inp2 = input("what is your string :")
# l2 = user_inp2.count("")
# print("---count of charecters----", (int(l2)-1))
#
""" 3. String slicing """

# user_inp3 = input("what is your string :")


""" 3.Length of longest string in pytho """

# str_ ="my name is anjali i am from luknow ".split()
# li = []
# conv = list(str_)
# for char in conv:
#     len_ = (len(char))
#     update = li.append(len_)
# print(max(li))

""" 4. First last chars swapping"""

# user_inp4 = input("what is your string :")
# empty_str = ""
# conve_ = list(user_inp4)
# conve_[0],conve_[-1] = conve_[-1],conve_[0]
# conve_2 = empty_str.join(conve_)
# print(str(conve_2))

""" 5. Remove odd index values """


# we_know = input("random words : ")
# b= we_know[1::2]
# print("----ofteer removing words be ---- : ", b)


""" 6. Count words in a string """

# cou_str = input("what is your string :")
# emp_list = list(c)
# b = cou_str.count()
# c = emp_list.join(b)
# print("------count-----",emp_list)


""" 7. Upper lower case of a string """

# user_choice = input("what you want to convert to Upper : ")
# result = user_choice.upper()
# result_2 = user_choice.lower()
# print("----upper caser are----:","\n",result)
# print("----lower caser are----:","\n",result_2)


""" 8.Last part of string """
# user_name = input("what is your choice of entry : ")
# part_string = user_name[-1]
# print(part_string)

""" 9.Convert a given string to all uppercase """

# in_data = input("what is entry data : ")
# dat_up = in_data.upper()
# print("---ur upper case letter ----",dat_up)

""" 10.program to remove a newline in Python """

# lis = input("what is your choice in intresst : ")
# string = lis.strip()
# print(string)


""" 11.program to check whether a string starts with specified characters """

y = input("choice of your string : ")
z = input("which letter you want to check starts or not : ")
check_ = y.startswith(z)
print(check_)

""" to set the indentation of the first line """

""" 12.to print the following floating numbers upto 2 decimal places """


""" 13.print the following floating numbers upto 2 decimal places with a sign """

# usr_choice_1 = float(input("what is your first number : "))
# usr_choice_2 = float(input("what is your second number : "))
# usr_choice_3 = input("what is your operation : ")
# add = "+"
# sub = "-"
# div = "/"
# multi = "*"
#
# if usr_choice_3 == add:
#     b = float(usr_choice_1) + float(usr_choice_2)
#     c = round(b,2)
#     print("addintion is ",c)
# if usr_choice_3 == sub:
#     b = float(usr_choice_1) - float(usr_choice_2)
#     c = round(b,2)
#     print("substraction is ",c)
# if usr_choice_3 == multi:
#     b = float(usr_choice_1) * float(usr_choice_2)
#     c = round(b,2)
#     print("multiplication is ",c)
# if usr_choice_3 == div:
#     b = float(usr_choice_1) / float(usr_choice_2)
#     c = round(b,2)
#     print("division is ",c)
# # b = round(usr_choice_1,2)
# else:
#     print("please enter valid perfomance ")

# x = [[(1,2),(3,4),(10,25)]]
# i = []
# b = x[0]
# c = b[0]
# d = b[1]
# e = b[2]
# f = list()
# print(c,d,e)
# for i in x:
#     i = list(i)
#     i = i.index(i)
#     print(i)

# n = 5
# i =0
# my_list = []
# while i < 5:
#     i = i +1
#     i =my_list.append(i)
#     print(i)



""" to display a number with a comma separator """
# my_choice = int(input("enter a number to check  : "))
# b = my_choice.lstrip(3)
# print(b)

""" to format a number with a percentage """

# number1 = int(input("what is your first number : "))
# number2 = int(input("what is your second number : "))
# result = ((number2) /(number1))*100
# result1 = round(result,2)
# print("--your percentage is--",result1,"%")


""" to count occurrences of a substring in a string """

""" 14.count repeated characters in a string """
# str_1 = input("user choice : ")
# a = []
# for i in str_1:
#     if i != i :
#         a = list(i)
#         print(a)
# print("repeated ",i)

""" 15.print the index of the character in a string """


""" 16.convert a string in a list """
# user_1 = input("what is your choice of string : ")
# c = list(user_1)
# b = user_1.rsplit()
# print(c)

# what_is = input("what is your name : ")
# a = list(what_is)
# print(a)

""" 17.swap comma and dot in a string """
""" 18.count and display the vowels of a given text """

# user_choice = input("what is your choice of text : ")
# user_choice ="ramesh"
# vowels = ["a","e","o","i","u"]
# for i in user_choice:
#     for j in vowels:
#         if i == vowels:
#             print(i)
#     print(vowels)

""" 19.remove spaces from a given string """
# user_1 = input("what is your data entry : ")
# b1 = user_1.rstrip()
# print(b1)

""" 20.move spaces to the front of a given string """

# a= "anjali    "
# res = a.rsplit()
# print(res)

""" 21.capitalize first and last letters of each word of a given string """

# user_inp = input("what is your name : ")
# f_upr = user_inp.capitalize()
# l_upr = f_upr[-1].upper()
# res = f_upr[0:-1]+l_upr
# print(res)

""" 22.remove leading zeros from an IP address """
# ip_id = input("what is your ip adress : ")
# f_op = ip_id.replace("0", "" )
# print(f_op)

# inp_1 = input()
# inp_2 = input()
# res = inp_1.capitalize() + " " + inp_2.capitalize()
# url = input("wgah : ")
# rev = []
# c = rev.append(url)
# print(rev)

""" 25.String slicing """
# user = input("what is your strin : ")
# b = user[0:8:]
# print(b)

"""26.Length of longest string in python """
# user_1 = input("what is your choice of string : ")
# user_1 = " iam not welcoming any one "
# c = list(user_1)
# b = user_1.rsplit()
# print(b)

""" 27.First last chars swapping """
# user = input("tell me your name : ")
# b = user.reversed()
# print("your swaping is ",b)

""" Last part of string """



""" program to remove a newline in Python"""







""" to set the indentation of the first line """
""" to print the following floating numbers upto 2 decimal places """
""" print the following floating numbers upto 2 decimal places with a sign """



"""  to display a number with a comma separator """

# y = int(input("enter a value : "))
# z = "{:,}".format👍
# print(z)



"""  to format a number with a percentage """
# inp_1 = int(input("what is your first number : "))
# inp_2 = int(input("what is your second  number : "))
# devide = (inp_1/inp_2)*100
# print(devide,"%")


"""  to count occurrences of a substring in a string """

# user_random = input("what is your choice of words : ")
# check_letter = input("which letter you want to check : ")
# count_numbers = user_random.count(check_letter)
# print("your letter is repeated ",count_numbers)







""" print the index of the character in a string """
# user_choice = input("enter a words : ").split()
# user_index_choice = input("which words / letter index you want : ")
# li =[]
# result = user_choice.index(user_index_choice)
# print(result)




"""  convert a string in a list """
# user_choice = input("enter a words : ")
# li = []
# res = list(user_choice)
# print(res)

"""  swap comma and dot in a string """

""" remove spaces from a given string """
""" move spaces to the front of a given string"""

#3.Take a number as input from the user and print if the number entered is a prime number or composite number

for num in range(1,20):
    if num >1:
        for i in range(2,num):
            if (num %i)==0:
                # print("numner is ",num)

                break
    else:
        print("number is prime",num)