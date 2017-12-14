#!/usr/bin/env python3

#import parser

############################################################
#                                                          #
#        Program options. Feel free to modify them.        #
#                                                          #
############################################################

commentStartColumn = 80                                                        # Ideally a multiple of 4.
castleSize = 60

slcommentchar = "//"                                                           # The character that denotes a single line comment.
slcharByLang = {
    "python": "#",
    "javascript": "//",
    "c": "//",
    "cpp": "//",
    "c++": "//",
    "objective-c": "//",
    "c#": "//"
}
langByExtension = {
    "py": "python",
    "js": "javascript",
    "c": "c",
    "cpp": "cpp",
    "m": "objective-c",
    "c#": "cs"
}
disableKeywords = ""
castlekeyWords = ""
wallphrase = ""
fortphrase = ""

paddedCastles = True
reduceCastleSizeWithIndentation = True
minimumCastleSize = 40

commentStartColumn -= 1                                                        # Columns start at 1, the program starts at 0.

############################################################
#                                                          #
#                    Internal utilities.                   #
#                                                          #
############################################################

# Ready for parsing non-pythonic languages.
def getIndentation(string):                                                    # AKA Get indentation.
    firstActualChar = 0
    for character in range(1, len(string)):
        if(string[:character].strip() != ""):                                  # If all the following chars are spaces/padding, that's the last char.
            firstActualChar = character
            break
    return string[:firstActualChar-1]

# Ready for parsing non-pythonic languages.
def stripRight(string):
    lastActualChar = 0
    for character in range(0, len(string)):
        if(string[character:].strip() == ""):                                  # If all the following chars are spaces/padding, that's the last char.
            lastActualChar = character
            break
    return string[:lastActualChar]

def guessLang(fname):
    fname = fname.split(".")
    fname = fname[len(fname) -1]

    print("File extension: '{}'".format(fname))

    lang = None
    if(fname in langByExtension):
        lang = langByExtension[fname]
    
    while(lang not in slcharByLang):
        lang = input("Language unknown. Choose one of the following:").lower()
        print(slcharByLang.keys())
    
    print("Processing for language '{}'".format(lang))
    updateSLchar(slcharByLang[lang])

def updateSLchar(_slcommentchar):
    global slcommentchar
    global disableKeywords, castlekeyWords, wallphrase, fortphrase

    slcommentchar = _slcommentchar

    disableKeywords = [slcommentchar + " OCD Disabled", slcommentchar + " OCD Enabled"]
    castlekeyWords = [slcommentchar + " ocdcastle", slcommentchar + " !ocdcastle"]
    wallphrase = slcommentchar + " ocdwall"
    fortphrase = slcommentchar + " ocdfort "

