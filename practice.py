#1.6
def stringCompression(s):
	curCount = 1
	prevChar = s[0]
	toReturn = ""
	for i in range(1, len(s)):
		if s[i] == prevChar:
			curCount += 1
		else:
			toReturn += (prevChar + str(curCount))
			curCount = 1
			prevChar = s[i]
	toReturn += (prevChar + str(curCount))
	if len(toReturn) < len(s):
		return toReturn
	return s

print stringCompression("aabcccccaaa")
