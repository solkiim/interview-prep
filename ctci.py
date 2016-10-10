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
	
#1.2
def isPermutation(s1, s2):
	s1 = ''.join(sorted(s1))
	s2 = ''.join(sorted(s2))
	return s1 == s2
	
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
