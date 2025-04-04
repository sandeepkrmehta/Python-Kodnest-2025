import time
def print_number():
    for i in range(1,6):
        print(i)
        time.sleep(2)

def print_characters():
    for i in ['A','B','C','D','E']:
        print(i)
        time.sleep(1)

print_number()
print_characters()