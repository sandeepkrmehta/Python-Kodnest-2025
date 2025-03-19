userData = input("Enter list elements seperated by space: ") # 10 20 30 40
# print(userData.split())
# print('Code')


# Average Of Number in a list


li = userData.split()
li = []
for i in li:
    li.append(int(i))
print(sum(li)/len(li))


