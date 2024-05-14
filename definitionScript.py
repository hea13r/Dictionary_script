#!/usr/bin/env python3
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

#function to access api and return the json?
def wordSearch(x):
    apiUrl = "https://api.dictionaryapi.dev/api/v2/entries/en/"  # URL of the free dictionary, minus the word
    url1 = apiUrl + x
    response = requests.get(url1)
    return(response.json())


#function to return specific part of speech only, or all depending on user desires
def posReturn(rJson, pos): #pos stands for part of speech
    try:
        rJson[0]['word']
        for i in rJson:
            for meaning in i["meanings"]:
                if meaning['partOfSpeech'] == pos or pos == 0:
                    print("\n" + meaning["partOfSpeech"])  # This part prints the part of speech before each definition, so nouns, verbs, and all those will be in their own lists
                for definition in meaning["definitions"]:
                    if meaning['partOfSpeech'] == pos or pos == 0:
                        print('definition: ' + definition["definition"])  # this prints the actual definitions after "definition:"
        print()  # this adds a space between each part of speech
    except KeyError:
         print(rJson["title"] + ". " + rJson["message"])  # this gives the response from the site for not using a valid word
    print() #this might be unecessary, it was just meant to make it a bit cleaner, but i think it just adds too many blank lines right now. will probably update in a future..update

#function to return examples
#def exampleReturn(json, example):
#to be added in the future



def main():
    if len(argv) > 1:
        unkWord = argv[1]
        try:
            pos = argv[2]
        except IndexError:
            pos = 0
    else:
        userInput = input("\nEnter the word and part of speech separated by a space.\nIf you want all parts of speech, just enter a word.\n")  # Asks user for the word and stores it in unkWord
        try:
            unkWord, pos = userInput.split()
        except ValueError:
            unkWord = userInput
            pos = 0
    responseJson = wordSearch(unkWord)
    posReturn(responseJson, pos)

if __name__ == "__main__":
    main()
