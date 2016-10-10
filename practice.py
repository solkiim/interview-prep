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

print oneAway("pale", "pales")
