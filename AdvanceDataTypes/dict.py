# d1 = {key:value}
d1 = {
    'Name':'Sandepe',
    'Age': 24,
    'Phone':7261048972,
    'Math': 90,
    'Science': 90,
    'Name':'Siya',   #it replace the value name
    'ID': 101
    }

print(d1, type(d1))   # {'Name': 'Siya', 'Age': 24, 'Phone': 7261048972, 'Math': 90, 'Science': 90} <class 'dict'>

# Accessing dict values:
print(d1['Name']) # Siya
print(d1['Math']) # 90

for i in d1.keys():
    print(i, end=" ")   # Name Age Phone Math Science ID

print()

for i in d1.values():
    print(i, end=" ")   # Siya 24 7261048972 90 90 101 


print()

for i in d1.items():
    print(i)

''' Output
('Name', 'Siya')
('Age', 24)
('Phone', 7261048972)
('Math', 90)
('Science', 90)
('ID', 101)

'''
print()





'''
1.
2.
3.
4.
'''