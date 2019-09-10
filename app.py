import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w=w.lower()
    close = get_close_matches(w,data.keys(),n=1,cutoff=0.8)
    if w in data:
        return data[w]
    elif w.upper() in data:
        return data[w.upper()]
    elif w.capitalize() in data:
        return data[w.title()]
    elif len(close)>0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no." % close[0] )
        if yn =="Y":
            return data[close[0]]
        elif yn == "N":
            return "The Word doesn't exist. Please Double Check!"
        else:
            return "We didn't understatnd you entry."
    else:
        return "The Word doesn't exist. Please Double Check!"

word= input("Input word: ")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
