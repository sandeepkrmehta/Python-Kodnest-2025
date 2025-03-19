t1 = (10, 20,20, True, 'Code')
print(t1, type(t1))


# Accessing Specific Element from tuple:
print(t1[0]) # 10
print(t1[3]) # True


#t1[0] = 3000 //Not allowed


'''
1. Tuple stores Homogeneous as well as Hetrogeneous Type of Data.
2. Tuple is an ordered collection of data.
3. Tuple stores duplicate values.
4. Tuple is immutable(Once we create tuple we cannot modify it.)

'''

t2 = (100, 200, 300, 400)
e1, e2, e3, e4 = t2
print(f"e1: {e1}, e2: {e2}, e3: {e3}, e4: {e4}")     #output: e1 100, e2: 200, e3: 300, e4: 400

tup1 = (10, 20)
tup2 = (30, 40)
newtup = tup1 + tup2
print(newtup)  # (10, 20, 30, 40)
print(len(newtup))  # 4


sample_tup = (100, 200, 300)
del sample_tup