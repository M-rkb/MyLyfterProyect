def print_first_word():
	print("two!")
print_first_word()

def print_second_word():
	print("One!")
	print_first_word()
	return

print_second_word()

