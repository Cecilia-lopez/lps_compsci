
keepRunning = True
contacts_phone = {} 

print("Welcome to Contacts!") 
print("What would you like to do? Enter your choice and press 'enter'") 
 

while keepRunning: 
	print("(1) Add a phone number.") 
	print("(2) Print the full list of contacts.")
	print("(3) Enter a name to retrieve that contact's phone number.") 
	print("(0) Exit the Contacts app.")

	response = raw_input() 
	
	if response == "0": 
		keepRunning = False 

	elif response == "1":
		print("Ok, what's the name of your contact?") 
		contactName = raw_input() 
		print("What's the phone number of your contact?") 
		contactPhone = raw_input() 

		contacts_phone[contactName] = contactPhone  
	
	elif response == "2": 
	 	print(contacts_phone) 

	elif response == "3": 
		 print("Whose number would you like?")
		 name = raw_input() 
		 print(contacts_phone[name])  
			 
