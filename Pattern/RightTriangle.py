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