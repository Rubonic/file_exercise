num1 = 42 #variable declaration, number int
num2 = 2.3 #variable declaration, number float
boolean = True  #variable declaration, boolean
string = 'Hello World' #variable declaration, string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #var declaration, list of strings
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #var declaration, dictionary
fruit = ('blueberry', 'strawberry', 'banana') #tuple
print(type(fruit)) #log statement
print(pizza_toppings[1]) #log statement, access value of list
pizza_toppings.append('Mushrooms') #add value to end of pizza_toppings list
print(person['name']) #log statement, access value of person dictionary
person['name'] = 'George' #access and change value of name value in dictionary
person['eye_color'] = 'blue' # access and value value of 'eye_color value in dictionary
print(fruit[2]) = #log statement, access value of tuple

if num1 > 45: #conditional if
    print("It's greater") #log statement, string
else:   # else statement
    print("It's lower") #log statement, string

if len(string) < 5: #length check of string, conditional if
    print("It's a short word!") # log statement, string
elif len(string) > 15: #conditional else if, length check of string
    print("It's a long word!") #log statement, string
else: # conditional else
    print("Just right!") #log statement, string

for x in range(5): #for loop start, initialize var x
    print(x) #log statement, int , for loop stop
for x in range(2,5): #for loop start
    print(x) #log statement, int, for loop stop
for x in range(2,10,3): #for loop, increment by 3
    print(x) #log statement, int
x = 0 #varaible declaration, int
while(x < 5): #while loop
    print(x) #log statemnent
    x += 1 #increment

pizza_toppings.pop() #delete last value of list
pizza_toppings.pop(1) #delet value of list found and entered index

print(person) #log statement of dictionary
person.pop('eye_color') #remove value of key 'eye_color'
print(person) #log statement of dictionary

for topping in pizza_toppings: #for loop iterating through var toppings through pizza_toppings list
    if topping == 'Pepperoni':  #conditional if 
        continue #continue
    print('After 1st if statement') #log statement, string
    if topping == 'Olives': #conditional if 
        break #break from for loop 

def print_hello_ten_times(): #define function, no parameter
    for num in range(10): #for loop
        print('Hello') #log statement, string

print_hello_ten_times() #call function with no argument

def print_hello_x_times(x): #define function with parameter x
    for num in range(x): #for loop runs for x times
        print('Hello') # #log statement, string

print_hello_x_times(4) #call function, pass argument 4

def print_hello_x_or_ten_times(x = 10): #define function , with parameter x=10 if no argument passed
    for num in range(x): #for loop
        print('Hello') #log statement

print_hello_x_or_ten_times() #call function with no argument
print_hello_x_or_ten_times(4) #call function passing argument 4

#multiline comment
"""
Bonus section 
"""
#comments

#NameError: name <variable name> is not defined
# print(num3)

# num3 = 72

#TypeError: 'tuple' object does not support item assignment
# fruit[0] = 'cranberry'

#KeyError: 'favorite_team'
# print(person['favorite_team'])

#IndexError: list index out of range
# print(pizza_toppings[7])

#IndentationError: unexpected indent
#   print(boolean)

#AttributeError: 'tuple' object has no attribute 'append'
# fruit.append('raspberry')

#AttributeError: 'tuple' object has no attribute 'pop'
# fruit.pop(1)