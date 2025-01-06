/***
* 
*
*
* 
***/

def main():
	file_path = "books/frankenstein.txt"
	with open(file_path) as f:
		text = f.read()

	report_gen(text, file_path)

def word_count(text):
	return len(text.split())


def char_count(text):
	char_dict = {}
	for word in text:
		word = word.lower()
		if not word.isalpha():
			continue
		for char in word:
			if char not in char_dict:
				char_dict[char] = 1
			else:
				char_dict[char] += 1

	return char_dict


def report_gen(text, file_path):
	words = word_count(text)
	chars = char_count(text)
	sorted_chars = dict(sorted(chars.items(), key=lambda item: item[1], reverse=True))

	print(f"----- Begin report of {file_path} -----")
	print(f"{words} words found in the document") 
	print()
	
	for key, val in sorted_chars.items():
		print(f"The '{key}' character was found {val} times")
	
	print("----- End Report -----")	

main()
