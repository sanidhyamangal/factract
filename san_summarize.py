import summarizer # for getting a summary 
import re # for regex 
import wikipedia # to handdle wiki requests 

# function to remove garbage texts 
def remove_grabage(sent):
    return [x.strip() for x in re.split('=*= [a-zA-Z ]* =*=', sent) if x.split()]

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

    return clean_list

# main function for the mail 

if __name__ == "__main__":
    print(get_facts("narendra modi"))