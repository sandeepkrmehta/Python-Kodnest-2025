s1 = {10, 20 , 2, True, 'Code'}
print(s1, type(s1)) # output {True, 2, 20, 10, 'Code'} <class 'set'>

s1.add(500)
print(s1) #{True, 2, 20, 500, 10, 'Code'}

s1.remove(500)
print(s1)   # {'Code', True, 2, 20, 10}

st1 = {1,2,3}
st2 = {3,4,5}
new_set = st1.union(st2)

print(new_set)   #{1, 2, 3, 4, 5}

'''
1. In set we store Homogeneous as well hetrogenous type of Data.
2. Set is an unordered collection of Data beacuse set generates the 
output in random order. It does not mainain order of insertion in output.
3. Set cannot stores duplicate values.
4. Set is mutable means once we declare set, we can modify it.
'''