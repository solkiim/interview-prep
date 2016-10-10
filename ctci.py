# 1.1
def stringUniqueChars1(s):
	charsInString = set()
	for i in range(len(s)):
		if s[i] in charsInString:
			return False
		else:
			charsInString.add(s[i])
	return True

# 1.1 using no extra space
def stringUniqueChars2(s):
	s = ''.join(sorted(s))
	for i in range(len(s)-1):
		if s[i] == s[i+1]:
			return False
	return True
	
#----------------------------------------------------------------------
#1.2
def isPermutation(s1, s2):
	s1 = ''.join(sorted(s1))
	s2 = ''.join(sorted(s2))
	return s1 == s2
	
#----------------------------------------------------------------------
#1.3
def URLify(s):
	toReturn = ""
	if s == None or len(s) == 0:
		return toReturn
	arr = s.split()
	for i in range(len(arr) - 1):
		toReturn += (arr[i] + "%20")
	toReturn += arr[len(arr) - 1]
	return toReturn

#----------------------------------------------------------------------
#1.4
def palindromePermutation(s):
	s = s.lower().strip().replace(" ", "")
	charsUsed = {}
	for i in range(len(s)):
		if s[i] in charsUsed:
			charsUsed[s[i]] += 1
		else:
			charsUsed[s[i]] = 1
	numOdd = 0;
	for key, val in charsUsed.items():
		if val % 2 == 1:
			numOdd += 1
	if numOdd > 1:
		return False
	if len(s) % 2 == 1:
		return (numOdd == 1)
	return True

#----------------------------------------------------------------------
#1.5
def oneAway(s1, s2):
	if len(s1) == len(s2):
		return checkReplacement(s1, s2)
	elif abs(len(s1) - len(s2)) == 1:
		return checkInsertion(s1, s2)
	else:
		return False
		
def checkReplacement(s1, s2):
	countDiff = 0
	for i in range(len(s1)):
		if s1[i] != s2[i]:
			countDiff += 1
	return (countDiff <= 1)
	
def checkInsertion(s1, s2):
	shorter = ""
	longer = ""
	if len(s1) < len(s2):
		shorter = s1
		longer = s2
	else:
		shorter = s2
		longer = s1
	iShort = 0
	iLong = 0
	wasDiff = False
	while iShort < len(shorter):
		if longer[iLong] != shorter[iShort]:
			if not wasDiff:
				wasDiff = True
				iLong += 1
			else:
				return False
		else:
			iLong += 1
			iShort += 1
	return True

#----------------------------------------------------------------------
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

#----------------------------------------------------------------------
