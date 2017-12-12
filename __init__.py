#!/usr/bin/env python3

'''
OCDCommenter: A program to ensure code aesthetic.
Copyright (C) 2017 Gonzalo Ruiz aka RGON.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

############################################################
#                                                          #
#                          IMPORTS                         #
#                                                          #
############################################################

# Division required to perform ceil() and floor() with precision, and not just clip/round the values, which might lead to uneven line lengths.
from __future__ import print_function, division                                # Only needed for Python 2

import sys                                                                     # argv
import math                                                                    # ceil() and floor()
import shutil                                                                  # copy(i, o): preserve the backup file's mode and ownership.

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
fortKeyword = ""
wallkeyphrase = ""

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

    print("File extension:", fname)
    lang = None
    if(fname in langByExtension):
        lang = langByExtension[fname]
    
    while(lang not in slcharByLang):
        lang = input("Language unknown. Choose one of the following:").lower()
        print(slcharByLang.keys())
    
    print("Processing for language", lang)
    updateSLchar(slcharByLang[lang])

############################################################
#                                                          #
#                    Internal functions.                   #
#                                                          #
############################################################

def updateSLchar(_slcommentchar):
    global slcommentchar
    global disableKeywords, castlekeyWords, fortKeyword, wallkeyphrase

    slcommentchar = _slcommentchar

    disableKeywords = [slcommentchar + " OCD Disabled", slcommentchar + " OCD Enabled"]
    castlekeyWords = [slcommentchar + " ocdcastle", slcommentchar + " !ocdcastle"]
    fortKeyword = slcommentchar + " ocdfort"
    wallkeyphrase = slcommentchar + " ocdwall "


# Ready for parsing non-pythonic languages.
def analyzeCommentLine(line, startPos):
    # If the text inside the line (without taking into account the comment itself) isn't longer than the column where the comment should start.
    lineWithoutComment = line[:startPos]
    lineWithoutComment = stripRight(lineWithoutComment)

    comment = line[startPos:]

    idealStart = commentStartColumn
    if(len(lineWithoutComment) > commentStartColumn):
        idealStart = len(lineWithoutComment) + 4

    padding = idealStart - len(lineWithoutComment)

    return lineWithoutComment + (" "*padding) + comment

# Ready for parsing non-pythonic languages.
def getModdedLine(line):
    commentCharsFound = 0
    for character in range(0, len(line)):
        if(character+len(slcommentchar) > len(line)):                          # End of the line. Cannot seek past it.
            continue

        if (line[character:character+len(slcommentchar)] == slcommentchar):    # When a # is found.
            if(not (line[character-len(slcommentchar)] == "\\" and line[character-len(slcommentchar)-1] != "\\")):    # If it isn't escaped.
                if((commentCharsFound % 2) == 0):                              # If it isn't inside quotes.
                    if(character < len(line)-1):                               # Also, if it isn't the last character, and there's a comment.
                        line = analyzeCommentLine(line, character)
                        break                                                  # Comment found. Stop searching this line's chars.
                        # endif
                # endif
            # endif
        elif(line[character] == "'" or line[character] == '"'):
            if(not (line[character-1] == "\\" and line[character-2] != "\\")): # If it isn't escaped.
                commentCharsFound += 1
    # endfor

    return line

# Ready for parsing non-pythonic languages.
def castleBuilder(line):
    global castleSize

    strippedLine = line.strip()
    indentation = getIndentation(line)

    actualCastleSize = castleSize
    if (reduceCastleSizeWithIndentation):
        actualCastleSize = castleSize - len(indentation)
        if(actualCastleSize < minimumCastleSize):
            actualCastleSize = minimumCastleSize

    if(strippedLine == castlekeyWords[0] or strippedLine == castlekeyWords[1]):
        if(paddedCastles):
            line = line.replace(
                castlekeyWords[0], 
                slcommentchar*int(actualCastleSize/len(slcommentchar)) + "\n" + indentation + slcommentchar + " "*int(actualCastleSize - len(slcommentchar)*2) + slcommentchar).replace(
                
                castlekeyWords[1],
                slcommentchar + " "*int(actualCastleSize - len(slcommentchar)*2) + slcommentchar + "\n" + indentation + slcommentchar*int(actualCastleSize/len(slcommentchar)))
        else:
            line = line.replace(
                castlekeyWords[0], 
                slcommentchar*int(actualCastleSize/len(slcommentchar))).replace(
                
                castlekeyWords[1], 
                slcommentchar*int(actualCastleSize/len(slcommentchar)))
        
        return line
    else:
        # Remove any SLChar characters that might be left over in the start/end.
        line = line.strip()
        if(line[0:len(slcommentchar)] == slcommentchar):
            line = line[len(slcommentchar):]
        if(line[len(line)-len(slcommentchar):len(line)] == slcommentchar):
            line = line[:len(line)-len(slcommentchar)]

        line = line.strip()

        spacesToAdd = actualCastleSize - len(line) - (len(slcommentchar)*2)    # mind the slcommentchars
        
        if(spacesToAdd <= 0):
            spacesToAdd = 2
        spacesToAdd /= 2
        
        # Int required in python2.
        line = indentation + slcommentchar + " "*int(math.ceil(spacesToAdd)) + line + " "*int(math.floor(spacesToAdd)) + slcommentchar + "\n"
        return line

# Ready for parsing non-pythonic languages.
def fortBuilder(line):
    line = line.replace(fortKeyword, slcommentchar*int(castleSize/len(slcommentchar)))
    return line

def wallBuilder(line):
    strippedLine = line.strip()[len(wallkeyphrase):]
    indentation = getIndentation(line)

    strippedLine = " " + strippedLine + " "

    actualCastleSize = castleSize
    if (reduceCastleSizeWithIndentation):
        actualCastleSize = castleSize - len(indentation)

    charactersToAdd = actualCastleSize - len(strippedLine)
    
    if(charactersToAdd <= 8):
        charactersToAdd = 8
    charactersToAdd /= 2

    charactersToAdd /= len(slcommentchar)

    line = indentation + slcommentchar*int(math.ceil(charactersToAdd)) + strippedLine + slcommentchar*int(math.floor(charactersToAdd)) + "\n"
    return line

############################################################
#                                                          #
#                Main program functionality.               #
#                                                          #
############################################################

# Ready for parsing non-pythonic languages.
def ocdFile(_infile, _outfile):
    _outfile = open(_outfile, 'w')

    '''
    try:
        _outfile = open(_outfile, 'w')
    except:wallBuilder
        pass
    '''
    
    with open(_infile) as f:
        print("Processing file.")
        tempdisabled = False
        buildcastle = False

        for line in f.readlines():
            line = line.replace("\t", " "*4)                                   # Tab to spaces.

            strippedLine = line.strip()                                        # Remove indentation.
            
            analyzeThisLine = True

            if(not len(strippedLine)):                                         # The line is empty. Avoid errors.
                analyzeThisLine = False
            else:
                if(strippedLine[0:len(slcommentchar)] == slcommentchar):       # If it isn't the first character in the line, aka the line isnt't a comment.
                    analyzeThisLine = False
                    
                    if(not tempdisabled):
                        if(strippedLine == castlekeyWords[0]):
                            buildcastle = True
                        if(buildcastle):
                            line = castleBuilder(line)                         # Redefined

                            if(strippedLine == castlekeyWords[1]):
                                buildcastle = False
                    
                        if(strippedLine == fortKeyword):
                            line = fortBuilder(line)                           # Redefined
                        elif(strippedLine[:len(wallkeyphrase)] == wallkeyphrase):
                            line = wallBuilder(line)

                    if(strippedLine == disableKeywords[0]):
                        tempdisabled = True
                    elif(strippedLine == disableKeywords[1]):
                        tempdisabled = False
                
                if(tempdisabled == True):
                    analyzeThisLine = False                                    # Forcefully disabled.    

            if(analyzeThisLine):
                line = getModdedLine(line)
            
            print((line), file=_outfile, end="")
        print("Done.")

# Ready for parsing non-pythonic languages.
def checkSyntax(_file):                                                        # Before letting castleBuilder break a file, check if there are any syntax errors and prevent that.
    with open(_file) as f:
        print("Checking file syntax.")

        buildingcastle = False
        lastOcurrence = None

        for i, line in enumerate(f.readlines()):
            strippedLine = line.strip()                                        # Remove indentation.
            line = strippedLine + getIndentation(line).replace("\t", "    ")   # Tab to spaces.
            
            if(len(strippedLine)):                                             # The line is empty. Avoid errors.
                if(strippedLine[0:len(slcommentchar)] == slcommentchar):       # If it isn't the first character in the line, aka the line isnt't a comment.
                    if(strippedLine == castlekeyWords[0]):
                        if(buildingcastle):
                            print("ERROR @ line {}: File contains an unclosed castle tag.".format(i+1))
                            print("Line content: {}".format(line.strip()))
                            print("Last ocdcastle tag found @ line {}".format(lastOcurrence))
                            print("\nQuitting right now.")
                            quit()
                        else:
                            buildingcastle = True
                            lastOcurrence = i
                    elif(strippedLine == castlekeyWords[1]):
                        if(buildingcastle):
                            buildingcastle = False
                            lastOcurrence = i
                        else:
                            print("ERROR @ line {}: File contains a closing castle tag, but no new castle has been started.".format(i+1))
                            print("Line content: {}".format(line.strip()))
                            print("Last ocdcastle tag found @ line {}".format(lastOcurrence))
                            print("\nQuitting right now.")
                            quit()
        
        if(buildingcastle):
            print("ERROR: File contains an unclosed castle tag.")
            print("Last ocdcastle tag found @ line {}".format(lastOcurrence))
            print("\nQuitting right now.")
            quit()

        print("File contains no improperly placed tags.")
        
        # Not checking for "OCD-Disabling" tags, as they're harmless.
        '''
        if(strippedLine == disableKeywords[0]):
            tempdisabled = True
        elif(strippedLine == disableKeywords[1]):
            tempdisabled = False
        '''

# Ready for parsing non-pythonic languages.
def processFile(fname):
    guessLang(fname)

    checkSyntax(fname)
    backupFileName = fname + ".bak"

    print("Backing up original file.")
    shutil.copy(fname, backupFileName)

    ocdFile(backupFileName, fname)                                             # Read the backed up file, edit the actual file. This maintains the file's permissions.

############################################################

# Ready for parsing non-pythonic languages.
if(__name__ == "__main__"):
    arguments = sys.argv
    
    ########################################################
    #                                                      #
    #                   Precarious UI.                     #
    #                                                      #
    ########################################################

    print()
    
    if(len(arguments) == 2):
        fname = arguments[1]
    else:
        fname = input("Drop your file here -> ").strip().replace("'", "").replace('"', "")

    processFile(fname)

    print()