print("How much does the nachos cost?") 
nacho_price = int(raw_input()) 
print("How much money do you have in your pocket?") 
cash = int(raw_input()) 

if nacho_price > cash: 
	print("Sorry, no nachos for you") 
if nacho_price <= cash: 
	print("Woot, nachos!")
if nacho_price == cash: 
	print("That sure was lucky!")  
print("Thanks for using nacho-buyer.py.") 
