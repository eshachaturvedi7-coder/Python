a = int(input("Enter your age: "))
#if elif else ladder
if(a>=20):
    print("your are above the age of consent")
    print("good for you")
    
elif(a<0):
    print("you are entering an invalid negative age")
    
elif(a==0):
    print("you are entering 0 which is not a valid age")
    
else:
    print("you are below the age of consent")
    
print("end of the program")