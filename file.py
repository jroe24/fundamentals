num1 = 42 #variable declaration, number
num2 = 2.3 #variable declaration, float
boolean = True #boolean
string = 'Hello World' #variable declaration, string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #variable declaration, list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #variable, #dictionary
fruit = ('blueberry', 'strawberry', 'banana') #variable declaration, tuple
print(type(fruit)) #type check, tuple
print(pizza_toppings[1]) #tuple, access value
pizza_toppings.append('Mushrooms') #tuple, add value
print(person['name']) #tuple , access value
person['name'] = 'George' #dictionary, change value
person['eye_color'] = 'blue' #dictionary, change vlaue
print(fruit[2]) #dictionary, access value

if num1 > 45: #conditional, if statement
    print("It's greater") 
else: #conditional, else statement
    print("It's lower")

if len(string) < 5: #conditional, if statement
    print("It's a short word!")
elif len(string) > 15: #conditional, else if statement
    print("It's a long word!")
else: #conditonal, else statement
    print("Just right!")

for x in range(5): #for loop
    print(x)
for x in range(2,5): #for loop
    print(x)
for x in range(2,10,3): #for loop
    print(x)
x = 0 #initialize
while(x < 5): #while loop
    print(x)
    x += 1 #increment

pizza_toppings.pop() #index error
pizza_toppings.pop(1) #remove index 1 from list

print(person)
person.pop('eye_color') #remove 'eye_color' from person
print(person)

for topping in pizza_toppings: #for loop
    if topping == 'Pepperoni': #if statement
        continue #continue
    print('After 1st if statement') 
    if topping == 'Olives': #if statement
        break #break loop

def print_hello_ten_times(): #calling function
    for num in range(10): #for loop
        print('Hello')

print_hello_ten_times()

def print_hello_x_times(x): #calling function
    for num in range(x): #for loop
        print('Hello')

print_hello_x_times(4) #access index 4 in print_hello_x_times

def print_hello_x_or_ten_times(x = 10): #call function, initialize x
    for num in range(x): #for loop
        print('Hello')

print_hello_x_or_ten_times() #tuple
print_hello_x_or_ten_times(4) #index 4 in print_hello_x_or_ten_times


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)