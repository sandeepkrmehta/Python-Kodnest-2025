s1 = "This is a test. This test is simple.".replace('.'," ").split()
print(s1)
di = {}
for i in s1:
    for i in di:
        di[i] = di[i] + 1
    else:
        di[i] = 1 
# print(di - dictonary)
for key in di.keys():
    print(f'{key}: {di[key]}')