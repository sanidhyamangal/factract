import summarizer # for getting a summary 
import re # for regex 
import wikipedia # to handdle wiki requests 
from pyteaser import SummarizeUrl, Summarize
import collections #for counting the most counted word
from collections import Counter

# function to get important facts 
def get_facts(user_input):
    text_desc = wikipedia.page(user_input).content
    text_title = wikipedia.page(user_input).title 

    # facts for the above article 
    summ = summarizer.summarize(title=text_title, text=text_desc, count=30)

    # clean summ from garbage values 
    clean_list = [] # empty list for the cleaned facts

    for s in summ:
        clean_list.append(remove_grabage(s)[0].replace("\n", " "))
    
    summ_txt = ' '.join(word.encode('utf-8') for word in clean_list[:10])
    summ_txt = summ_txt.replace(". ", ".\n\n")
    
    return summ_txt

#--------------------------------------------------------------------------------------------------------------------

def fact_extract(user_input):

	#user_input = str(raw_input('Enter input: ')) this will come from the front end instead of cli
	url = wikipedia.page(user_input).url

	# s = Summarize(user_input, wikipedia.page(user_input).content) is to summarize if the url is not available
	# this one is for extracting the content directly from the keyword entered by the user
	s = SummarizeUrl(url)

	summ = ' '.join(word for word in s)
	#summ = summ.replace("]","")

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

	summ = removeNestedParentheses(summ)
	summ = summ.replace(". ",".\n\n")
	
	return summ
