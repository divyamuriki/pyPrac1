# lower_value = int(input("Please, Enter the Lowest Range Value: "))
# upper_value = int(input("Please, Enter the Upper Range Value: "))
#
# print("The Prime Numbers in the range are: ")
# for number in range(lower_value, upper_value + 1):
#     if number > 1:
#         for i in range(2, number):
#             if (number % i) == 0:
#                 break
#         else:
#             print(number)

def prime_number(n):
    c = 0
    for x in range(2, n):
        if n % x == 0:
            c = c + 1
    return c


n = int(input("Enter a number = "))
if prime_number(n) == 0:
    print("Prime number.")
else:
    print("Not prime number.")