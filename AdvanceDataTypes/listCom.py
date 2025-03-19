li = [10, 20, 30, 40, 50, 50]

sqList = []

for i in li:
    sqList.append(i ** 2)
    print(i ** 2)
print(f"Square List: {sqList}")  # [100, 400, 900, 1600, 2500, 2500]



# another Method

print(f"Square list: {[i ** 2 for i in li]}")  # [100, 400, 900, 1600, 2500, 2500]


# for unique List

unique_list = list(set(li))
unique_sqlist = list(set(sqList))    
print(unique_list)               # [40, 10, 50, 20, 30]
print(unique_sqlist)                 # [1600, 900, 2500, 100, 400]


#WAP to add +5 to each element of li and create new list of it.
print([i + 5 for i in li])   # [15, 25, 35, 45, 55, 55]


#WAP to print list of even element from li1;

li1 = [1, 2, 3, 4, 5]
even = [i for i in li1 if i % 2 == 0]
print(even)  # [2, 4]


# [experssion for control_variable in iterable_object condition]


