from bs4 import BeautifulSoup
import wikipedia

# import sys

# reload(sys)
# sys.setdefaultencoding('utf8')


def make_card(user_input):

	pg = wikipedia.WikipediaPage(title=user_input)
	pghtml = pg.html()

	soup = BeautifulSoup(pghtml, 'html.parser')
	table = soup.table
	heads = table.findAll('tr')
	info_box = []

	for head in heads[:7]:
		info_box.append(head.get_text())

	#non reg ex way of dealing with expressions
	def removeNestedParentheses(s):
	    ret = ''
	    skip = 0
	    for i in s:
	        if i == '[':
	            skip += 1
	        elif i == ']'and skip > 0:
	            skip -= 1
	        elif skip == 0:
	            ret += i
	    return ret

	# summ_list = []
	# st_list = []
	# for summ in info_box[1:]:
	# 	summ_list.append(summ.replace("\n",":"))
	# for st in summ_list:
	# 	st = removeNestedParentheses(st)
	# 	#print st
	# 	st_list.append(st)
	# return st_list[1:]
	for x in range(7):
		info_box[x] = removeNestedParentheses(info_box[x])
	return info_box[1:]
	# return info_box

# print make_card("Narendra Modi")