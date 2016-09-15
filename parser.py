file=open("occupations.csv", "r")
stringthing = file.read()
splitString = str.split(stringthing, "\r\n")
dict = {}

for line in splitString:
    if line[0] == '"':
        line = line[1:]
        
        

print(s)
file.close()
