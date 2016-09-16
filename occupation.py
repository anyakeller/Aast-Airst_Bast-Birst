import random
# Opens and reads file into stringthing
file=open("occupations.csv", "r")
stringthing = file.read()

# Splits the string into an array called splitString
splitString = str.split(stringthing, "\r\n")

dict = {}

# Loops through array line by line
for line in splitString:
	if "Total" not in line:
		if len(line)>0 and line[0]=='"':
			line = line[1:]
			dict[float(line[line.index('"')+2:])]=line[0:line.index('"')]
		elif len(line)>0 and splitString.index(line)!=0:
			#print line
			dict[float(line[line.index(',')+1:])]=line[0:line.index(',')]
        
#print dict

#because we have to make this a function...
def getRandomOccupation():
	#get a random number from 0 to 997 <-- although the toal is 99.8, we're working with integers and randint() is inclusive of zero
	r = random.randint(0,997)
	temp = 0 #keeps track of probability range
	for key in dict:
		temp += 10 * key
		if r < temp:
			return dict[key]
		if temp == 859:
			return dict[key]

print getRandomOccupation()



file.close()
