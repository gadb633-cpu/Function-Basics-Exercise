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
    print(f"the result is: {a*b}")
multiply(5)
multiply(8,56)    
# 7
def print_largest(a,b,c):
    if a >= b and a >= c:
        print(f"the largest is: {a}")
    elif b >= a and b >= c:
        print(f"the largest is: {b}")
    elif c >= a and c >= b:
        print(f"the largest is: {c}")
print_largest(3,8,5)
print_largest(10,2,7)
print_largest(4,4,1)
# 8
def show_fahrenheit(c):
    print(f"converts Celsius to Fahrenheit is: {(c*9/5)+32}")

show_fahrenheit(0)
show_fahrenheit(100)
show_fahrenheit(37.5)
