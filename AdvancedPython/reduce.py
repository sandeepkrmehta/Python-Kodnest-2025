from functools import reduce

li = [1,2,3,4,5]
def sum(a, b):
    return a + b

sum_result = reduce(sum,li)
print(sum_result)