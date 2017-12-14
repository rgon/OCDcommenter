# OCDcommenter

A perfect soultion for coders whose OCD has them worried about their code's comment aesthetics. No more time wasting, I've already done that for you.

OCDcommenter automatically spaces all your inline comments to occupy a certain column, making them look better and without having you waste time doing it.
Because many are the times when one notices that this block's comments aren't indented to the same level as the previous one's.

This is what you write:
```
from __future__ import print_function, division    # Only needed for Python 2
import sys  # argv
import math   # ceil() and floor()
```
And this is what you get:
```
from __future__ import print_function, division                                # Only needed for Python 2
import sys                                                                     # argv
import math                                                                    # ceil() and floor()
```
Much cleaner, just running the script. Rejoice.

Smart enough so you needn't worry about it. The program detects if it's a comment line, if the comment is the last element of the line, if it's inside quotes, if it's an escaped character, if the line's longer than the comment column... 

And, BTW, it changes all tabs to 4 spaces.

## Usage:
Just run `OCDcommenter/__init__.py` and drag your script to it (or append it as the script parameter). It'll do the hard work for you.
You may include this as a libary on your program, provided that you respect the license (read LICENSE.md).
_Your original file is backed up as *filename*.bak, so you can always revert one level._

## Supported languages:
The program detects the language based on the file's extension. If it's unknow, it prompts the user for a choice.
* Python (2/3) [*.py]
* JavaScript [*.js]
* C (C99/C11 or later, not compatible with ANSI-C) [.c]
* C++/C#/Objective-C [.cpp, .cs, .m]


## Tools:

### OCDcastle
Easily build good title blocks to divide sections of your code.
```
############################################################
#                                                          #
#             Look! I'm a section of this code!            #
#                                                          #
############################################################
```
Gets rendered when you write:
```
# ocdcastle
# Your content goes here.
# !ocdcastle
```
or
```
////////////////////////////////////////////////////////////
//                                                        //
//           I wanna build a castle outta wood.           //
//                                                        //
////////////////////////////////////////////////////////////
```
Produced by writing:
```
// ocdcastle
// I wanna build a castle outta wood.
// !ocdcastle
```


### OCDfort
Smaller code dividers.
```
############################################################
Or in Javascript/C:
////////////////////////////////////////////////////////////
```
Produced by:
```
# ocdfort
For JS or C, use:
// ocdfort
```


### OCDwall
Useful for differentiating between groups of elements/functions inside a class.
```
###################### This is a wall. #####################

# ocdwall This is a wall.
```
Produced by: `
```
# ocdwall This is a wall.
For JS or C, use:
// ocdwall This is a wall.
```


### Disabling the parser in a section of code.
OCDcommenter allows disabling the parser in certain sections if wanted.
```
# OCD Disabled
# Any content here won't be parsed. # So this string won't be spaced.
# Neither will this be processed.
# OCD Enabled
```


## Editor-agnostic.
This program is independant of your editor, so there's no need to worry about compatibility issues.

## License
This program is distributed under the GNU GPL v3 license.

## More info and help
Check out the files in [/Tests](../Tests).


Want a new feature? Contact me or perform a pull request. Anything that makes our lives simpler is welcome.
