text = "Hello my name is Sven"

count_words = text.split()
letters=0
for i in text:
	if i != " ":
		letters += 1
print(letters)

average = letters/len(count_words)
print(average)
