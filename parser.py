file=open("occupations.csv", "r")
stringthing = file.read()
splitString = str.split(stringthing, "\r\n")
dict = {}

for line in splitString:
    if len(line)>0 and line[0]=='"':
        line = line[1:]
        dict[line[0:line.index('"')]]=float(line[line.index('"')+2:])
    elif len(line)>0 and splitString.index(line)!=0:
        print line
        dict[line[0:line.index(',')]]=float(line[line.index(',')+1:])
        
print dict
file.close()
