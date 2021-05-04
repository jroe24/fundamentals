x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

def update_values(x, students, sports, z):
    x[1][0] = 15
    student[0]['last_name'] = "Bryant"
    sports['soccer'][0] = "Andres"
    z[0]['y'] = 30

update_values(x, students, sports_directory, z)


students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def iterate_dictionary(some_list):
    print_string = ""
    for item in some_list:
        for key, value in item.item():
            print_string += f"{key} - {value},"
            print(print_string)
            print_string =""

iterate_dictionary(students)

def iterate_dict(key_name, some_list):
    for some_dict in some_list:
        print(some_dict[key_name])

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)
# output:
7 LOCATIONS
San Jose
Seattle
Dallas
Chicago
Tulsa
DC
Burbank
    
8 INSTRUCTORS
Michael
Amy
Eduardo
Josh
Graham
Patrick
Minh
Devon

def printInfo(some_dict):
    for key in some_dict: #loop through dictionary
    print(f"{len(some_dict[key])} {key.upper()}")
    for item in some_dict[key]:
        print(item)
        print() #Prints blank line for spacing

print_info(dojo)


