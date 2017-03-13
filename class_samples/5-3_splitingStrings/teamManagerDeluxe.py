# This part of the code is used to create the object
class Player(object): 
  def __init__(self, name, age, goals, jersey_number, position): 
    self.name = name 
    self.age = age 
    self.goals = goals 
    self.jesrey_number = jersey_number 
    self.position = position 
 
 # This block of code is used to have the statistics of the players that have been added to the team  
  def getStats(self): 
    stats = "name: " + self.name + "\n" 
    stats = stats + "age: " + str(self.age) + "\n" 
    stats = stats + "goals: " + str(self.goals) + "\n" 
    stats = stats + "Jersey Number: " + str(self.jersey_number) + "/n" 
    stats = stats + "Position: " + str(self.position) + "/n" 

    return stats

# Saves the teams 
def saveTeam(myPlayers, filename)
        # Opens the file to write in it and save the data  
	my_file = open(filename, "a") 
	# Creates a loop so that all the players in the file are saved 
	for p in myPlayers: 
		my_file.write(p.name + " " + str(p.age) + " " + str(p.goals) + " " + str(p.jersey_number) + " " + p. position + "\n")
 	# Closes the file 
	my_file.close() 
  

    
# This creates  a list , and adds the players that have been added     
players = [] 

keepRunning = True 

# this part of the code gives the different options to the users 
while keepRunning: 
  print("What would you like to do? Enter your choice and press 'enter'.")
  print("(1) Add a player.") 
  print("(2) Print players.") 
  print("(0) Leave the program and delete all players.") 
  
  response = input() 

# This part of the code gets implemented when the user inputs 0, and the program stops running   
  if response == 0: 
    keepRunning = False 

# This part of the code gets implemented when the user inputs 1, and it allows the user to add a new player to the soccer team    
  elif response == 1: 
    print("Ok, enter the players name and press enter.") 
    teamPlayer = raw_input()
    print("How old is the player?") 
    playerAge = input() 
    print("How many goals has this player scored?") 
    playerGoals = input() 
   
# This part of the code adds the new player to the list of the other players in the team 
    myplayers = Player(teamPlayer, playerAge, playerGoals) 
    players.append(myplayers) 
    print("Ok, got it! View your players again to see it!")

# This last block of code is implemented when the user inputs 2, and the program prints the information of all the players in the list  
  elif response == 2: 
    for p in players: 
      print(p.getStats())
      
 
