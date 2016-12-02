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


# breadth first traversal
def bft(root):
	q = queue()
	q.enqueue(root)
	while not q.isEmpty():
		node = q.dequeue()
		visit(node)
		q.enqueue("node's children")

# depth first traversal
def dft(root):
	visit(root)
	if root.left != None:
		dft(root.left)
	if root.right != None:
		dft(root.right)
