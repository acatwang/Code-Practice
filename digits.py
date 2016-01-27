import random,re
class Game(object):
	def __init__(self):
		self.answer = self.getAnswer()
		self.finish = False
		self.attemps = 0
		self.guesses = []

	def getAnswer(self):
		# Non repeat!
		return ''.join(str(x) for x in random.sample(xrange(0,9),4))

	def guess(self,inputs):
		if inputs == 'peek':
			return "Answer is: " + self.answer
		valid, msg = self.sanify(inputs)
		if not valid:
			return msg
		
		correct, hint = self.check(inputs)
		if correct:
			self.finish = True
		
		return hint

	def sanify(self,nums):
		# Make sure the input are 4 distinct digit
		shows = [0] * 10
		for i in nums:
			if i.isdigit():
				if shows[int(i)] :
					return (0,'Found repeated digit: %s' % i)
				shows[int(i)] = 1
			else:
				return(0, 'Numbers only') 
		return (1,'Pass')

	def check(self,digits):
		a,b,hint = 0,0, ''
		for i,num in enumerate(digits):
			if num == self.answer[i]:
				a +=1
			elif num in self.answer:
				b +=1
		hint = 'You got it' if a==4 else '{0} A {1} B'.format(a,b)
		return (a==4, hint)

if __name__ == '__main__':
	game = Game()
	while not game.finish:
		inputs = raw_input("Enter your guess: ")
		print game.guess(inputs)
