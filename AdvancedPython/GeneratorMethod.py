def disp():
    print("Start")
    yield 10
    print("Task 1")
    yield 20
    print("Task 2")
    yield 30

res = disp()


# 1st method
# for i in range(2):
#     print(res.__next__())

# another method Exceptions
for i in res:
    try:
        print(res.__next__())
    except:
        print("There is not next value available stop this iterations")