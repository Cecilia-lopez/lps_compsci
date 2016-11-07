print("Hours in New York?") 
NewYorkHours = int(raw_input())
print("Minutes in New York?") 
NewYorkMinutes = int(raw_input())

Californiatime = int(NewYorkHours - 3)
if NewYorkHours == 1:
	Californiatime = 10
elif NewYorkHours == 2:
	Californiatime = 11
elif NewYorkHours == 3: 
	Californiatime = 12  

print("If the time in New York is " + str(NewYorkHours) + ":" + str(NewYorkMinutes) + " , then the time in california is " + str(Californiatime) + ":" + str(NewYorkMinutes) + ".") 


