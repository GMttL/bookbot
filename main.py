def main():
	with open("books/frankenstein.txt") as f:
		text = f.read()
	
	#print(text)
	#print(word_count(text))
	print(char_count(text))

def word_count(text):
	return len(text.split())


def char_count(text):
	char_dict = {}
	for word in text:
		word = word.lower()
		for char in word:
			if char not in char_dict:
				char_dict[char] = 1
			else:
				char_dict[char] = char_dict[char] + 1

	return char_dict


main()
