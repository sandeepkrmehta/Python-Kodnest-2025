#Increasing Star Pattern
rows = int(input('Enter Number of Rows: ')) # taking an input

# 1st method

# row = int(input('Enter Rows: '))
# for i in range(1, row+1):
#     print("*" * i)


# 2nd method


for i in range(rows):
    for j in range(i+1):
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

# Decreasing Star Pattern

# rows = int(input('Enter Number of Rows: '))

# for i in range(rows):
#     for j in range(5 - i):
#         print("*", end=" ")
#     print()

# output:
# Enter Number of Rows: 5
# * * * * * 
# * * * * 
# * * * 
# * * 
# * 
print(" ")  # Space betweem them

for i in range(rows):
    for j in range(i, rows):
        print("*", end=" ")
    print()


# output: 
# * * * * *
# * * * *
# * * *
# * *
# *

print(" ")  # Space betweem them

for i in range(rows):
    for j in range(i , rows):
        print(' ', end=" ")
    for k in range(i + 1):
        print("*", end=" ")
    for m in range(i):
        print("*", end=" ")
    print()

# output: 
#           *
#         * * *
#       * * * * *
#     * * * * * * *
#   * * * * * * * * *


print(" ")  # Space betweem them

for i in range(rows):
    for j in range(i + 1):
        print(' ', end = " ")
    for k in range(i, rows):
        print("*", end=" ")
    for m in range(i, rows - 1):
        print("*", end=" ")
    print()


# output :
#   * * * * * * * * *
#     * * * * * * *
#       * * * * *
#         * * *
#           *