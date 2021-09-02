#IMPORT STATEMENTS
import requests


#constants
meaning_error = False
example_error = False

#Take Input From User

word = input("Tell me a word  ").lower()
OWN_Endpoint = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
response = requests.get(OWN_Endpoint)
try:
    response.raise_for_status()
except:
    print("Please Check The spelling. Or Browse the web")
    meaning_error = True

word_data = response.json()


if(meaning_error == False):
        word_slice = word_data[0]["meanings"][0]['definitions'][0]['definition']
        print(word_slice)


try:
    word_example = word_data[0]["meanings"][0]['definitions'][0]['example']
except:
    example_error = True

if (example_error == True):
    no_example = "No Example present"
    print(no_example)
    word_example = "NULL"
else:
    print(word_example)


comments = input("Please provide maunal input  ")
note = "NULL"
if(comments=="NULL"):
    pass
else:
    print(comments)
    note = comments