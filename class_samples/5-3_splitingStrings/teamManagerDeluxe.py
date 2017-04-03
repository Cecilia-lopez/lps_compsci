# This part of the code is used to create the object
class Player(object): 
  def __init__(self, name, age, goals, jersey_number, position): 
    self.name = name 
    self.age = age 
    self.goals = goals 
    self.jersey_number = jersey_number 
    self.position = position 
 
 # This block of code is used to have the statistics of the players that have been added to the team  
  def getStats(self): 
    stats = "name: " + self.name + "\n" 
    stats = stats + "age: " + str(self.age) + "\n" 
    stats = stats + "goals: " + str(self.goals) + "\n" 
    stats = stats + "Jersey Number: " + str(self.jersey_number) + "\n" 
    stats = stats + "Position: " + str(self.position) + "\n" 

    return stats

# Saves the teams 
def saveTeam(myPlayers, filename):
        # Opens the file to write in it and save the data  
	my_file = open(filename, "a") 
	# Creates a loop so that all the players in the file are saved 
	for p in myPlayers: 
		my_file.write(p.name + " " + str(p.age) + " " + str(p.goals) + " " + str(p.jersey_number) + " " + p. position + " ")
 	# Closes the file 
	my_file.close() 

def loadTeam(filename):
	# create an empty list
	empty_list = []
	# open file to read it
	my_file = open(filename, "r")
	# read each line of the file
	my_line = my_file.readline()
	# make a loop
	while my_line != "":
		# split the lines of the file so it becomes a list
		myWords = my_line.split()
		# add to the list 
		empty_list.append(Player(str(myWords[0]), str(myWords[1]), str(myWords[2]), str(myWords[3]), str(myWords[4]) + "\n"))
		# ask for the next line of the file and repeat the same things 
		my_line = my_file.readline()
	        # close the file
	        my_file.close()
	        # return the list
	        return empty_list  

  

keepRunning = True 

# ask the user what they want to do
print("Welcome to Team Manager Deluxe!")
print("Do you want to start with a new team or open an existing team?")
print("Enter the # of your choice")
print("(1) Start with a new team")
print("(2) Open a file for an existing team")
# allow them to choose
choice = raw_input()

# if their choice is 2, then we should load the file team
if choice == "2":
	# ask what the name of the file is
	print("What's the filename for your existing team? Enter the whole name, including its .tmd exetension")
	# allow them to input it
	filename = raw_input()
	# load their team
	myPlayers = loadTeam(filename)
# else if they choose 1, start with a new team
else:
	myPlayers = []



# this part of the code gives the different options to the users 
while keepRunning: 
  print("What would you like to do? Enter your choice and press 'enter'.")
  print("(1) Add a player.") 
  print("(2) Print players.")
  print("(3) Save your player list to a file.")  
  print("(0) Leave the program.(save first to avoid losing your data!)") 
  
  response = input() 

# This part of the code gets implemented when the user inputs 0, and the program stops running   
  if response == 0: 
    keepRunning = False 

# This part of the code gets implemented when the user inputs 1, and it allows the user to add a new player to the soccer team    
  elif response == 1: 
    print("Ok, enter the players name and press enter.") 
    name = raw_input()
    print("How old is the player?") 
    age = raw_input() 
    print("How many goals has this player scored?") 
    goals = raw_input() 
    print("What is the jersey number?") 
    jersey_number = raw_input()
    print ("What position does the player play?") 
    position = raw_input()
    
# This part of the code adds the new player to the list of the other players in the team 
    myPlayers.append(Player(name, age, goals, jersey_number, position))
   
    print("Ok, got it! View your players again to see it!")

# This last block of code is implemented when the user inputs 2, and the program prints the information of all the players in the list  
  elif response == 2: 
    for p in myPlayers: 
      print(p.getStats())

# This block gets implemented when the user inputs 3, and it saves the players in a file 
  elif response == 3:
	# ask what they want to name it
	print("What will be the name of your file? Enter the name, including the .tmd extension.")
	filename = raw_input()
	# save their players and file
	saveTeam(myPlayers, filename)

      
 
