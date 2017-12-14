#!/usr/bin/env python3
# This program will, in a future version, be able to reverse a rendered file to ocdwall keywords.
'''
OCDcommenter: A program to ensure code aesthetic.
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

from . import *

############################################################
#                                                          #
#                Main program functionality.               #
#                                                          #
############################################################

# Ready for parsing non-pythonic languages.
def reverseFile(_infile, _outfile):
    _outfile = open(_outfile, 'w')

    '''
    try:
        _outfile = open(_outfile, 'w')
    except:
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
                            print("castle")

                            if(strippedLine == castlekeyWords[1]):
                                buildcastle = False
                    
                        if(strippedLine == wallphrase):
                            line = wallBuilder(line)                           # Redefined
                        elif(strippedLine[:len(fortphrase)] == fortphrase):
                            line = fortBuilder(line)

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
def processFile(fname):
    guessLang(fname)

    backupFileName = fname + ".bak"

    print("Backing up original file.")
    shutil.copy(fname, backupFileName)

    reverseFile(backupFileName, fname)                                             # Read the backed up file, edit the actual file. This maintains the file's permissions.

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
    print("This is the reverser. It's just the oposite of parser.")
    
    if(len(arguments) == 2):
        fname = arguments[1]
    else:
        fname = input("Drop your file here -> ").strip().replace("'", "").replace('"', "")

    processFile(fname)

    print()