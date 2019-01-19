import wikipedia

user_input = str(raw_input('Enter the user query: '))

page = wikipedia.page(user_input)
#print page.content.encode('utf-8')
print wikipedia.summary(user_input, sentences = 1).encode('utf-8')