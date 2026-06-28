# part_1
# 1
def greet(name):
    print("hello:",name)
greet("agent X")
# 2
def add(a,b):
    print(a + b)
add(3,4)
# 3
def square(n):
    print("square n is: ",n**2)
square(5)
square(12)
# 4
def greet_with_title(name,title="agent"):
    print("hello:",title,name)
greet_with_title(name="gad")
greet_with_title(name="yossi",title="groom")
# 5
def describe(name,level,active):
    print(f"name is:{name} level is:{level} active is:{active}")
describe(level=10,active=False,name="yossi")
# 6
def multiply(a,b=2):
    print(a*b)
multiply(5)
multiply(8,56)    

