#Python program to print
#even numbers in a list using recursion
def evennumbers(list, n=0):
	#base case
	if n==len(list):
		exit()
	if list[n]%2==0:
		print(list[n], end=" ")
	#calling function recursively
	evennumbers(list, n+1)
list1 = [10, 21, 4, 45, 66, 93]
print("Even numbers in the list:", end=" ")
evennumbers(list1)
