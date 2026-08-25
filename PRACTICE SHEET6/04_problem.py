#write a program to find whether a given username contains less than 10 characters or not

username = input("enter username: ")

if(len(username)<10):
    print("your username contain less than 10 characters")
    
else:
    print("your username contains more than or equal to 10 characters")