#4.1
def routeBetweenNodes(n1, n2):
	q = queue()
	n1.visited = true
	q.enqueue(n1)
	
	while not q.isEmpty():
		node = q.dequeue()
		if node == n2:
			return True
		for neighbor in node.neighbors:
			if not neighbor.visited:
				neighbor.visited
				q.enqueue(neighbor)
	return False
	
#----------------------------------------------------------------------

#4.2
def findMinimalTree(arr):
	return findMinimalTreeHelper(arr, 0, len(arr))

def findMinimalTreeHelper(arr, start, end):
	if end < start:
		return null
	root = node()
	mid = (start + end) / 2
	root.val = arr[mid]
	root.left = findMinimalTree(arr, 0, mid - 1)
	root.right = findMinimalTree(arr, mid + 1, len(arr))
	return root
	
#----------------------------------------------------------------------

#4.3
def listDepths(root):
	depthlist = []
	q = queue()
