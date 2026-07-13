marks ={
    "esha":90,
    "paridhi":95,
    "ashna":96
    
}

print(marks) # prints the dictionary of marks
print(type(marks)) # prints the type of the variable marks
#methods
print(marks.items()) # prints the items of the dictionary
print(marks.keys()) # prints the keys of the dictionary
marks.update({"esha":94}) # updates the value of the key "esha"
print(marks) # prints the updated dictionary of marks
print(marks.get("esha")) # prints the value of the key "esha"