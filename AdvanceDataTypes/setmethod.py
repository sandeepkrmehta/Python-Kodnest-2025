s1 = {1, 2, 3,4,5}
s2 = {3,4,5,6,7,8}
new_set = s1.symmetric_difference(s2)
print(new_set)  # {1, 2, 6, 7, 8}


# subset (issubset method return true or false)

st1 = {10,20,30}
st2 = {10,20,30,40,50}
print(st2.issubset(st1)) #false
print(st1.issubset(st2))  #True