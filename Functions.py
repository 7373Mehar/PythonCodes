#Creating A Function
def my_name(name, age):
    print("Hello " + name + ", you are " + str(age))

my_name("Mehar", 21)
my_name("Barry Allen", 34)

#Return Statements
def my_name(name, age):
    return("Hello " + name + ", you are " + str(age))

print(my_name("Mehar", 21))
print(my_name("Barry Allen", 34))

#Return Statement
def cube(num):
    return num*num*num
print(cube(3))
