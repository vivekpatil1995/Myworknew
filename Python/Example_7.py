# Built-in string functions

# isalnum()
# Returns true if string has at least 1 character and
# all characters are alphanumeric and false otherwise.
#  isalpha()
# Returns true if string has at least 1 character and
# all characters are alphabetic and false otherwise.
# isdigit()
# Returns true if string contains only digits and false otherwise.


def fun():
	first="hello"
	print(first.isalnum())
	print(first.isalpha())
	print(first.isdigit())

	second="hello8"
	print(second.isalnum())
	print(second.isalpha())
	print(second.isdigit())

	third="200"
	print(third.isalpha())
	print(third.isalnum())
	print(third.isdigit())
fun()
