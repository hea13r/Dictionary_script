import json
import requests
from sys import argv

##################################################################################
#										                                         #
#                    Basic Dictionary Script                                     #
#         This script asks the user for a word they want the definition of       #
#        It will then append that word to the free dictionary API URL            #
#       Then it will request the definitions of that word from free dictionary   #
#   It gets a json back, and then iterates over the json to get the definitions  #
#   It will then print, sorted by part of speech, the definitions                #
#    It also checks to make sure the user entered a real word                    #
#    If a real word is not entered it will return the error from the site        #
#  I'm sure there is plenty of room for improvement, like the try, except used   #
#         To be used from a command line, not sure how to make GUIs yet		     #
#										                                         #
##################################################################################

apiUrl = "https://api.dictionaryapi.dev/api/v2/entries/en/"  # URL of the free dictionary, minus the word

# can use the command line option of adding the word after the script to search right away in this fashion: python3 definitionScript.py word
# if nothing is added on the command line it will ask user what word to search
if len(argv) > 1:
    unkWord = argv[1]
else:
    unkWord = input("\nWhat word do you want the definition for? ")  # Asks user for the word and stores it in unkWord


fullUrl = apiUrl + unkWord  # appends the word to the URL

response = requests.get(fullUrl)  # API request for the word, stored in response

responseJson = response.json()  # stores the response in json format

try:  # This will attempt to find a "title" in the response, if it's there it will provide the "no valid word" response from the site
    responseJson["title"]  # if a valid word is used there is not "title" in the response, so that's what I used
    print(responseJson["title"] + ". " + responseJson["message"])  # this gives the response from the site for not using a valid word
    print()
except TypeError:  # There is no "title" when a valid word is used, so it gives this error
    for i in responseJson:  # The format from the response is weird, it was a list with dictionaries in it, so I had to iterate over it with for loops
        for meaning in i["meanings"]:
            print("\n" + meaning["partOfSpeech"])  # This part prints the part of speech before each definition, so nouns, verbs, and all those will be in their own lists
            for definition in meaning["definitions"]:
                print('definition: ' + definition["definition"])  # this prints the actual definitions after "definition:"
    print()  # this adds a space between each part of speech
