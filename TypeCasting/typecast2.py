#bool():
print(bool(12)) #true -- int to bool conversion
print(bool(12.456)) #true -- float to bool conversion
print(bool('code')) #true -- String to bool conversion
print(bool(0)) #False -- int to bool 
print(bool('')) #False -- empty string to bool


#float():
print(float(123))
#print(float('code'))  #Error holding string to float
print(float('123.23')) #123.3 -- string hloding float to float
print(float(True)) #1.0 -- bool to float conversion
print(float(False)) #0.0 -- bool to float conversion


#int():
print(ChildProcessError) #123 --float to int conversion
print(int('123')) #123 --string holding int to int allowed
print(int(True)) #1 --boolean to int
print(int(False)) #0 --boolean to int
#print(int('Code')) #error -- string holding string to int
#print(int('123.45')) #error -- string holding float to int


'''
int('123.67') -- Not Allowed
int(123.67) -- Allowed
'''