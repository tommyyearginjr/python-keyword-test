import keyword

x = raw_input("Enter a word, to test whether or not it is a Python keyword: ")

if keyword.iskeyword(x):
    print("The word '{}' is a Python keyword.".format(x))
else:
    print("The word '{}' is not a Python keyword.".format(x))
