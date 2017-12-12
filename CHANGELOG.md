December 12th, 2017

Version 0.1: basic functionality implemented.
Version 0.2: added ocdcastles.
Version 0.3: added forts.
Version 0.3.5: put all the interface functions inside a __name__ == __main__ condition, to allow using the program as a module.
    Now the program can be called every time your program is saved, VS Code doesn't break a sweat, and it can be easily run.
Version 0.4: new file saving approach, maintains permissions, so there's no longer any need to use chmod on the new file (linux).
Version 0.4.5: added an option to reduce the castle size if it's indented. Also added a minimum size.
Version 0.5: added syntax checking. Prevents the program from garbling your file.
Version 0.5.5: Changed the ocdcastle closing tag format. Better suited for languages that use forward slashes for commenting out text.

Version 1.0: Javascript Support (aswell as C/C++, they use the same single-line comment format).
Version 1.0.5: FIXED BUG: castles are not ignored.
Version 1.1: language detection by extension.
Version 1.1.5: added js test files, bad python file, proper python file.
Version 1.2.0: fixed "building a castle using the foundation of another", aka removing remnant comment characters from the lines of a castle.
Versoin 1.2.5: added a precarious CLI.
Version 1.3.0: added python2 support. Had to modify a couple of things.
Version 1.3.5: fixed the tab to spaces script. If run at this same program, the "tab" space in the replace() clase would get replaced by 4 spaces.