
import random
myNum = random.randint(1,1000)

print("I am thinking of a number between 1-1000. Enter a guess!") 
guess = int(raw_input())
takes = 1  
while guess !=  myNum: 
	if guess > myNum: 
		print("Nope. Too high! Guess again.") 
      		guess = int(raw_input())
		takes = takes + 1 
	elif guess < myNum:
		print("Nope. Too low! Guess again.") 
		guess =int(raw_input())
		takes = takes + 1 
if guess == myNum:
	print("Good job! You guessed right after " + str(takes) + " tries.")  
	 
