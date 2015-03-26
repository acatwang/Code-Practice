"""
Use python list to make stack and queue
===============
Stack: last in first out (push/pop)
Queue: first in first out (enqueue/dequeue)
http://www.cs.cmu.edu/~adamchik/15-121/lectures/Stacks%20and%20Queues/Stacks%20and%20Queues.html

"""

# The list itself can be used as stack
stack = []
stack.append(1)
stack.append(5)
stack.append(7)
stack.pop()
print stack


# To implement queue,
# One can also use collection.deque
class Queue:
	def __init__(self):
		self.l =[]

	def enqueue(self,n):
		self.l.append(n)
		return self.l

	def dequeue(self):
		self.l.pop(0) # remove the 1st element
		return self.l
	def show(self):
		print self.l


queue = Queue()

queue.enqueue(1)
queue.enqueue(5)
queue.enqueue(7)
queue.dequeue()
queue.show()