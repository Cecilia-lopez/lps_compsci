print("What number do you want multiples for?")
maximum = 1 
number = float(raw_input())  
multiples = 0 
while maximum < 1000:
	maximum = number * multiples  
	multiples = multiples + 1 
	print( str(number) + "times " + str(multiples) + " is eqial to " + str(maximum)) 
  	if maximum >= 1000: 
		print("Those are all the multiples up to 1,000.") 
