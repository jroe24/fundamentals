def countdown(x):
    if x >= 0:
        print(x)
        countdown(x-1)

countdown(5)

def print_and_return(a,b):
    print(a)
    return(b)

print_and_return(1,2)

def first_plus_length(my_list5):
    return(my_list5[0] + len(my_list5))

list1 = [1,2,3,4,5]
x = first_plus_length(list1)
first_plus_length(list1)
print(x)

def values_greater_than_second(list1):
    new_list = []
    for x in list1:
        if x > list1[1]:
            new_list.append([x])
    if len(new_list) < 2:
        return False
    else:
        print(len(new_list))
        return new_list

list1 = [3,5,6,7,8,9]

y = values_greater_than_second(list2)
print(y)

def length_and_value(a, b):
    new_list = []
    x = a
    for x in range(a):
        if x > 0:
            new_list.append([b])
            x-1
        else:
            return new_list

y = length_and_value(2, 3)
print(y)