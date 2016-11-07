fave = 8  
print("Guess any number?") 
user_input = int(raw_input()) 

if user_input ==  fave:
	print("Wow, you guessed it! You must be a genius.")
if user_input != fave: 
	print("Sorry you lose, try again!")  

if user_input < fave:
	print("Try a higher number.") 
if user_input > fave:
	print("Try a lower number.") 
