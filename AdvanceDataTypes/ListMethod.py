li = []
li = [50]
# Adding Element into List(at the end of the list) using append():
li.append(100)
li.append(200)
print("After Append: ",li)   #[50, 100, 200]

#insert(index, element) inserts and element at specific index
li.insert(0, 400,)
print("After Insert: ", li) # [400, 50, 100, 200]

# pop() : Pop method without any argument removes and returns last element from the list.
ele = li.pop()
print("After Pop: ", ele) # 200
print("After ele: ", li)  #[400, 50, 100]

#pop (index): Pop can remove specific index element from list.
print("AFter pop Index: ",li.pop(1))  # 50
print("AFter pop : ",li) # [400, 100]

li.append(700) 
print("Updated list: ", li)  #[400, 100, 700]

# remove(element): Removes element from list
li.remove(700)
print("After Remove: ", li)  #[400, 100]

li.append(900) 
print("Updated list: ", li) #[400, 100, 900

# del keyword:
del li[1]
print("After del: ", li) #[400, 900]

del li # Deletes whole object from the memory
# print(li) # Error