# function that is going to help find prime numbers amongts a lot of numbers 
def Prime(star, list):
	term = range(1,int(star))
	rat = star - 2 
	start = 0 
	for number in term: 
		tiger = int(star) % int(number) 
# This part of the code is going to test is the number is going to be prime 
		if tiger != 0: 
			start = start + 1
# This section of the code is going to happen the number does not have a remainder 
			if start == rat:
				print(star)
				list.append(star)
# This function makes an empty list 
primenumList = []
numList = range(1,10000)
# This part prints out the prime numbers 
for stop in numList: 
	sky = Prime(stop, primenumList) 
