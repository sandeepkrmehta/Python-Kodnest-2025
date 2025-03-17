# 1st method

# row = int(input('Enter Rows: '))
# for i in range(1, row+1):
#     print("*" * i)


# 2nd method

row = int(input('Enter Rows: '))
for i in range(1, row+1):
    for i in range(i):
        print("*", end = " ")
    print()

# output: 
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 


#Number printing
# row = int(input('Enter Rows: '))
# for i in range(1, row+1):
#     for j in range(1, i + 1):
#         print(j, end = " ")
#     print()

# output
# 1 
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# 1 2 3 4 5 6