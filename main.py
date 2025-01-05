def main():
	with open("books/frankenstein.txt") as f:
		file_contents = f.read()
	
	print(file_contents)
	
	print(word_count(file_content))

def word_count(text):
	return len(text.split())


main()
