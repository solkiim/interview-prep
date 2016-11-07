def bracketCheck(str):
	bracketDict = {'(':')', '{':'}', '[':']'}
	closingBrackets = bracketDict.values()
	s = stack()
	
	for i in range(len(str)):
		if str[i] in bracketDict:
			s.push(str[i])
		else if str[i] in closingBrackets:
			if s.isEmpty():
				return False
			else if bracketDict[s.pop()] != str[i]:
				return False
	
	if not s.isEmpty():
		return False
	
	return True
	
# time complexity: O(n)
# space complexity: O(n)
