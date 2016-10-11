#2.1
def removeDups(head):
	alreadyIn = set()
	alreadyIn.add(n.val)
	n = head
	while (n.next != None):
		if n.next.val in alreadyIn:
			n.next = n.next.next
		else:
			alreadyIn.add(n.next.val)
		n = n.next
	return head
	
#----------------------------------------------------------------------

#2.2
def kthToLast(head, k):
	pointer1 = head
	pointer2 = head
	for i in range(k):
		pointer1 = pointer1.next
	while pointer1.next != None:
		pointer1 = pointer1.next
		pointer2 = pointer2.next
	return pointer2
	
#----------------------------------------------------------------------

#2.3
def deleteMiddle(middle):
	n = middle
	n.val = n.next.val
	n.next = n.next.next
	return n
	
#----------------------------------------------------------------------

#2.4
def partition(node, x):
	head = head
	tail = head
	while (node.next != None):
		if node.val < x:
			node.next = head
			head = node
		else:
			tail.next = node
			tail = node
		node = node.next
	tail.next = None
	return head
	
#----------------------------------------------------------------------

#2.5
def sumLists(head1, head2):
	toReturn = head1
	toReturnStart = toReturn
	while (head1.next != None and head2.next != None):
		sumval = head1.val + head2.val
		carry = sumval / 10
		nodeval = sumval % 10
		toReturn.val = nodeval
		head1.next.val += carry
		head1 = head1.next
		head2 = head2.next
		toReturn = toReturn.next
	if head2.next != None:
		toReturn.next = head2
	return toReturnStart

#----------------------------------------------------------------------

#2.6
def palindrome(head):
	start = head
	end = head
	stack = stack()
	
	while end.next != None and end != None:
		stack.push(start.val)
		start = start.next
		end = end.next.next
	if end != None:
		start = start.next
	while start.next != None:
		if stack.pop() != start.val:
			return False
		start = start.next
	return True

#----------------------------------------------------------------------

#2.7
def intersection(head1, head2):
	end1 = head1
	end2 = head2
	length1 = 0
	length2 = 0
	while end1.next != null:
		end1 = end1.next
		length1 += 1
	while end2.next != null:
		end2 = end2.next
		end2 += 1
	if end2 != end1:
		return None
	if end2 - end1 > 0: # end2 is bigger
		for i in range(end2 - end1):
			head2 = head2.next
	else if end1 - end2 > 0:
		for i in range(end1 - end2):
			head1 - head1.next
	while head1.next != null:
		if head1 == head2:
			return head1
		head1 = head1.next
		head2 = head2.next
	return None

#----------------------------------------------------------------------

#2.8
def loopDetection(head):
	alreadyIn = set()
	while n.next not in alreadyIn:
		n = n.next
	return n.next
