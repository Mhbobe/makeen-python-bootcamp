
mynumber = [1, 2, 3, 4]
print(mynumber)

mynumber.reverse()
print(mynumber)

print("----------------------------------------------------")

def my_list(num):
    return list(dict.fromkeys(num))
    
mynumber = my_list ([1, 2, 2, 3, 4, 1, 5])
print(mynumber)

print("----------------------------------------------------")

numbers = [4, 5, 6, 6, 7, 4, 8]

unique_number = list(set(numbers))

print(unique_number )

print("----------------------------------------------------")

def number(n):
    return [int(n) for n in str(n)][::1]

print(number(56789))


print("----------------------------------------------------")

mylist = [1, 2, 'a', 'b']

def filter_list(mylist):
    new_roster = []
    for x in mylist:
        if type(x) == int:
            new_roster.append(x)
    return new_roster

print(filter_list(mylist))