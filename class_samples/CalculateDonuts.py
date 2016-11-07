print("How many people wil you have at your party?") 
people = int(raw_input())
print("How many donuts will you have at your party?") 
donuts = int(raw_input())

print("Our party has " + str(people) +  " people and " + str(donuts) + " donuts.") 

receive = donuts / people 
 
print("Each person at the party gets " + str(receive) + " donuts.") 
