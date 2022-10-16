food = ["Burger", "Cheeze", "Bread"]
print(food)

mylist = ['Sahil', 20, "Abc", "25"]
print(mylist)

# Functions of List 
numlist = [10,50,20,40,11,25,80,90]
print("List before reversing",numlist)
numlist.reverse()
print("List after reversing",numlist)
numlist.sort()
print("List after sorting",numlist)
print(numlist)
print("Maximum = ",max(numlist))
print("Minimum = ",min(numlist))

# Slicing of List
num = [50,20,40,11,25]

print(num[0])
print(num[0:4])
print(num[:])
print(num[1:])
print(num[3:])
print(num[::])
print(num[::2])

# Manipulating(changing elements) the list
numbers = [2,7,4,3,5,11,13]
print(numbers)

numbers.append(7)
print(numbers)

numbers.insert(3,35)
print(numbers)

numbers.remove(13)
print(numbers)

numbers[0] = 8
print(numbers)