"""
Challenge: Reverse words in a sentence

"""
import sys

def reverse_word(sentence):

	words = sentence.split(' ')
	r_sentence = "".join([word+" " for word in words[::-1]])

	return r_sentence.rstrip(" ")

def main():
	#test_cases = open(sys.argv[1], 'r') # For CodeEval test
	test_cases = ["Hello World\n", "Hello CodeEval",""] # For local test
	for test in test_cases:
		print reverse_word(test.strip('\n'))

if __name__ == "__main__":
	main()