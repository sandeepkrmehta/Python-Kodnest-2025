s1 = 'hello'
s2 = 'World'
print('Address of l in s1:',id(s1[2]))
print('Address of l in s1:',id(s1[3]))
print('Address of l in s2:',id(s2[3]))

# print("Address of 'o' in s1: ", id(s1[1]))
# print(s1,id(s2))

print("Address of 'o' in s1: ", id(s1[4]))
print("Address of 'o' in s2: ", id(s2[1]))

print(s2,id(s2))