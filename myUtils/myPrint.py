def printTable(table):
	counter = 0
	left = 0
	right = 0
	tmp = ""
	while (counter < len(table) - 2):
		counter += 1
		if table[counter] == "(":
			left = counter
		if table[counter] == ")":
			right = counter
			for i in range(left + 1,right):
				tmp += table[i]
			print tmp
			tmp = ""

def printTableToTXT(table):
	counter = 0
	left = 0
	right = 0
	tmp = ""
	file = open("skrypty\\testtest.txt","w")
	while (counter < len(table) - 2):
		counter += 1
		if table[counter] == "(":
			left = counter
		if table[counter] == ")":
			right = counter
			for i in range(left + 1,right):
				tmp += table[i]
			tmp+="\n"
			file.write(tmp)
			tmp = ""	
	file.close()

def printTableToCSV(table):
	counter = 0
	left = 0
	right = 0
	tmp = ""
	file = open("skrypty\\testtest.csv","w")
	while (counter < len(table) - 2):
		counter += 1
		if table[counter] == "(":
			left = counter
		if table[counter] == ")":
			right = counter
			for i in range(left + 1,right):
				tmp += table[i]
			tmp+="\n"
			file.write(tmp)
			tmp = ""	
	file.close()