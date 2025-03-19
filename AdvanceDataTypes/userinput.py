userData = input("Enter list elements seperated by space: ") # 10 20 30 40
# print(userData.split())
# print('Code')


# Average Of Number in a list


li = userData.split()
newli = []
for i in li:
    newli.append(int(i))
print(sum(newli)/len(newli))


