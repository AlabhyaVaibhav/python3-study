	#Single-Linked-List
	class Node:
	 	"""The fundamental structure of a linked list"""
	 	def __init__(self):
	 		self.head = None
	 		self.data = None
	 		self.next = None
	 	#This definition sets the data in the Node
	 	def setData(self,data):
	 		self.data = data
	 	#This definition returns the data from the Node	
	 	def getData(self):
	 		return self.data
	 	#This definition sets/points to the next Node in the linked list
	 	def setNext(self):
	 		self.next = next
	 	#This definition returns the next field of the Node
	 	def getNext(self):
	 		return self.next
	 	#This definition returns a TRUE if there exists a node next to the current one.
	 	def hasNext(self):
	 		return self.next != None
	 	'''Basic operation in a Linked List 
	 		1) Traversal 
	 		2) Insertion of Nodes 
	 		3) Deletion of Nodes
	 	'''
	 	#This definition finds the length of the linked list
	 	def listLength(self):
	 		current = self.head
	 		count = 0 
	 		while current != None:
	 			count = count + 1
	 			current = self.getNext()
	 		return count
	 	#Single Linked List Insertion
	 	''' Here only one pointer has to be updated 
			1) For an empty list 
			 _ _ _ _ _
	 		|data |   | -> none 
              ^--HEAD
            2 For a non empty list 
			 _ _ _ _ _      _ _ _ _ _      
	 		|data |   | -> | 51  |   | -> something cool stuff 
                              ^--HEAD
	 		 _ _ _ _ _      _ _ _ _ _      
	 		|data |   | -> | 51  |   | -> something cool stuff 
              ^--HEAD
	 	'''
	 	def insertAtBegining(self,data):
	 		newNode = Node()
	 		newNode.setData(data)
	 		if self.listlength() == 0:
	 			self.head = newNode
	 		else
	 			newNode.setNext(self.head)
	 			self.head = newNode 
	 	def insertAtEnd(self,data):
	 		newNode = Node()
	 		newNode.setData(data)
	 		current = self.head 
	 		while current.getNext() != None:
	 			current = current.getNext()
	 		current.setNext(newNode)
	 	def insertAtPos(self,pos,data):
	 		if pos > self.listlength() or pos < 0:
	 			return None
	 		else 
	 			if pos == 0:
	 				self.insertAtBegining(self,data)
	 			else:
	 				newNode = Node()
	 				newNode.setData(data)
	 				count = 0 
	 				current = self.head
	 				while current < pos:
	 					count = count + 1 
	 					current=current.getNext()
	 				newNode.setNext(current.getNext())
	 				current.setNext(newNode)












	 		 



