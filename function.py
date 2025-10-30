#function
# A function is the block of code when its called its run automatuically

# Parameter
# a parameter is the variable listed inside the parentheses in the function definition

#Argument
# An argument  is the value that is sent to the function when it is called

#define function

def fun():
    print("Hello")

#calling Fuction

fun()

#def Function_name(Parameters):
# statement(s)
#return(expression)


#Positional & Keyword Arguments

#Positional Argument

# This arguments are passed  based on their positions

def add_number(n1,n2):
    sum=n1+n2
    return sum
result=add_number(10,20)
print(result)

#Default Arguments

#default argument in Python is a function parameter that automatically takes a predefined value if no value is provided during the function call.
def add_number(n1=100,n2=200):
    sum=n1+n2
    return sum

result=add_number(5.4)
print(result)


#Keyword Argument
# A keyword argument in Python is when you pass a value to a function by specifying the parameter name, making the order of arguments unimportant.
#Here, age and name are keyword arguments.
def greet(name,age):
    print(f"name:{name},age:{age}")
greet(name="bala",age=25)

