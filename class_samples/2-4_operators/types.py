myName = 'Cecilia' 
myAge = 17 
isOld = False 

print('Here is the type for myName:') 
print(type(myName)) 
print('Here is the type for myAge:') 
print(type(myAge)) 
print('Here is the type for isOld:') 
print(type(isOld)) 

# this is correct 
print('My age is' + str(myAge))
#this throws an error 
print('My age is' + myAge) 
