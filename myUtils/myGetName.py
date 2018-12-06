def getName(string):
	length = len(string)
	tmp = ""
	for i in range(length-1,0,-1):
		if string[i] == "/":
			for j in range(i+1,length-4):
				tmp += string[j]
			break
	print tmp