print("Welcome to Netflix!")
print("Enter your 5 favorte TV shows.")
shows = 0 
my_list = []
while shows < 5:  
	print("Enter a show name:") 
	favorite = raw_input() 
	my_list.append(favorite)
	shows = shows + 1
print("okay, here's what you've entered:")  
print(my_list)
number = 1 
print("We've added a couple of important ones.") 
my_list.append("The Wire")
my_list.append("Breaking Bad")   
my_list.sort() 
for current_favorite in my_list:  
 	print(str(number) + ". " + current_favorite) 
	number = number + 1 
	
