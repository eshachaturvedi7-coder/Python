friend = ["apple","orange",5,345.67,True,"akash"]
print(friend) # prints the list
print(friend[0]) # prints the first element of the list
print(friend[1]) # prints the second element of the list
print(friend[5]) # prints the sixth element of the list
print(friend[1:4]) # prints the elements from index 1 to 3

#LIST METHODS
friend.append("banana") # adds an element to the end of the list
print(friend) # prints the list after adding an element
L1 = [1,2,3,4,5]
L1.extend([6,7,8]) # adds multiple elements to the end of the list
print(L1) # prints the list after extending it
L1.sort() # sorts the list in ascending order
print(L1) # prints the sorted list
L1.reverse() # reverses the order of the list
print(L1) # prints the reversed list
value = L1.pop() # removes the last element from the list and returns it
print(value) # prints the removed element
print(L1) # prints the list after removing the last element