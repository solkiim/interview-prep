def URLify(s):
	toReturn = ""
	if s == None or len(s) == 0:
		return toReturn
		
	arr = s.split()
	for i in range(len(arr) - 1):
		toReturn += (arr[i] + "%20")
	toReturn += arr[len(arr) - 1]
	return toReturn
	
print URLify("sol    kim  ")
