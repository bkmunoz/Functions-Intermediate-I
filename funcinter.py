#1.Update Values in Dictionaries and Lists
#Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
#Change the last_name of the first student from 'Jordan' to 'Bryant'
#In the sports_directory, change 'Messi' to 'Andres'
#Change the value 20 in z to 30

x = [ 
    [5,2,3], 
    [10,8,9]
] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

#def changeVal1(lst):
#    lst[1][0] = 15
#    return lst
#print(changeVal1(x))

#def changeVal2(lst):
#    lst[0]['last_name'] = 'Bryant'
#    return lst
#print(changeVal2(students))

#def changeVal3(dict):
#    dict['soccer'][0] = 'Andres'
#    return dict
#print(changeVal3(sports_directory))

#def changeVal4(lst):
#    lst[0]['y'] = 30
#    return lst
#print(changeVal4(z))

#2.Iterate Through a List of Dictionaries
#students = [
#        {'first_name':  'Michael', 'last_name' : 'Jordan'},
#        {'first_name' : 'John', 'last_name' : 'Rosales'},
#        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#        {'first_name' : 'KB', 'last_name' : 'Tonel'}
#    ]
#def iterateDictionary(some_list):
#    for x in range(len(some_list)):
#        print(f"First name - {some_list[x]['first_name']}, last name -{some_list[x]['last_name']}")

#iterateDictionary(students)
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
#first_name - Michael, last_name - Jordan
#first_name - John, last_name - Rosales
#first_name - Mark, last_name - Guillen
#first_name - KB, last_name - Tonel


#3.Get Values From a List of Dictionaries
#def iterateDictionary2(key_name, some_list):
#    for x in range(len(some_list)):
#        print(some_list[x][key_name])

#iterateDictionary2('first_name', students)
#iterateDictionary2('last_name', students)

#4.Iterate Through a Dictionary with List Values
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}



"""
#def Info(dict):
    for x in range(dict):
        return(len(dict[0]['locations']))

#def Info(dict):
    for x in range(dict):
        return(len(dict[x]['locations']))

print(Info(dojo))

#def Info(dict,key_name):
    for x in range(dict):
        return(len(dict[x]['key_name']))

#def Info(dict):
    return(len(dict[x]['key_name']))

#def Info(dict):
    return(len(dict[x][x]))

#def Info(dict):
    return(len(dict[list]))

#def Info(dict, key_name):
    print(dict[len('key_name')])

#def U(dict, key_name):
    print(dict[x][len('key_name')])

#def dictIterate(dict, key_name):
    dict[x][len('key_name')]
    print

#def dictIterate(dict):
    dict[x]['locations']

#def dictIterate(dict):
    for x in range (dict):
        dict[x]['key_name']
print(dictIterate)

#def dictIterate(dict):
    for x in range (dict):
        print(dict.get('locations', default=None))

#def dictIterate(dict):
    for x in range (dict):
        print(dict.get(key, default=None))

"""