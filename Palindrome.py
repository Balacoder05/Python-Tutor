name=input()
new=""
for i in name:
    new=i+new
    print(new)
if(name==new):
    print("Given name is palindrome")
else:
    print("Given name is not a palindrom")