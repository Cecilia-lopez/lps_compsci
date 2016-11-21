print("Welcome to Mario's and Luigi's Quest!") 
print("What is the name of your character?") 
character = raw_input()
print("Enter strength (1-10):")
strength = int(raw_input())
print("Enter health (1-10):") 
health = int(raw_input())
print("Enter luck (1-10):") 
luck = int(raw_input())


if (strength + health + luck) <= 15:
	print(str(character) + " has " + str(strength) + " points of strength, " + str(health) + " for health, and " + str(luck) + " for luck.") 
elif (strength + health + luck) > 15: 
	print("You gave your character too many points!") 
 	print("Default values have been assigned to " + str(character))     
	print("Strenth: 5 health: 5 luck: 5 ") 
print(character + ", you've come to a dead end. Do you want to go right or left? Enter 'right' or 'left'.") 
direction = raw_input() 

if direction == 'left' and health < 5:  
	print(character + " you have faced a scary clown. You have died of a heart attack because you're health was too weak.") 
	print("You have lost, try eating spinach next time.") 
elif direction == 'left' and health >= 5:    
	print(str(character) + " you have faced a scary clown. Hooray! You survived, you were healthy enough not to pass out.")
 	print("You are now walking, and come to a stop because of quick sand. You need to go around it. Do you want to turn left or right? Enter 'left' or 'right'.")
	turn_2 = raw_input() 
	if turn_2 == 'right' and luck >= 4:
	 	print("You have won! You were just lucky enough not to sink in the quick sand.") 
	elif turn_2 == 'right' and luck < 4:
		print("Sorry you lost, better luck next time.") 
	if turn_2 == 'left' and luck >= 5: 
		print("You have won! You were lucky enough not to sink in the quick sand.") 
	elif turn_2 == 'left' and luck < 5: 
		print("Sorry you lost, better luck next time.") 
if direction == 'right' and strength >= 6:
	print(str(character) + " you have come across a Dragon. Hooray! You have defeated the Dragon because you were strong enough.")
	print("Congatulations, you have won! Keep working out.")
elif direction == 'right' and strength < 6: 
	print(str(character) + " you have faced a Dragon. You have died, he was stronger than you.") 
	print("Sorry. Game Over.") 

