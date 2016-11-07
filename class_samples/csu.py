print("How many miles away do you live from Richmond State?") 
miles = int(raw_input()) 

print("what is your GPA?") 
GPA = float(raw_input())

if miles <= 30 and GPA >= 2.0: 
	print("Congratulations! You have been accepted to Richmond State!") 
elif  miles <= 30 and GPA < 2.0:
		print("Sorry you have not been admitted.")  

elif  miles > 30:
		print("What is your ACT score?") 
		ACT = int(raw_input())
		if GPA >= 2.5 and ACT >= 18:
			print("Congratulatons! You have been accepted!") 
	
		else:
			miles > 30 and GPA < 2.5 and ACT < 18 
			print("Sorry, you have not been admitted.") 

	
