print("Hi! What is your SAT score?") 
score = int(raw_input())

if score >= 1 and score < 1300: 
	print("Welcome to SAT prep!") 
elif score > 1300 and score < 1600:
	print("You probably don't need SAT prep.") 
elif score == 1600:
	print("WOW! You got a perfect score!") 
elif score > 1600: 
	print("Error! Score can not be higher than 1600.") 
