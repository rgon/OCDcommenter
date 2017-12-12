OCDCommenter
A perfect soultion for coders whose OCD has them worried about their code's comment aesthetics. No more time wasting, I've already done that for you.

OCDCommenter automatically spaces all your inline comments to occupy a certain column, making them look better and without having you waste time doing it.
Because many are the times when one notices that this block's comments aren't indented to the same level as the previous one's.

The program detects if it's a comment line, if the comment is the last element of the line, if it's inside quotes, if it's an escaped character... Smart enough so you needn't worry about it.

And, BTW, it changes all tabs to 4 spaces.

Usage:
Just run OCDCommenter/__init__.py and drag your script to it (or append it as the script parameter). It'll do the hard work for you.
Your original file is backed up as *filename*.bak, so you can always revert one level.
You may include this as a libary on your program, provided that you respect the license (read LICENSE.md).

Supported languages:
Works with python and javaScript files. Detects them based on their file extension. Asks the user when the extension is unknown.

Tools:
OCDcastle
Easily build good title blocks to divide sections of your code.

############################################################
#                                                          #
#             Look! I'm a section of this code!            #
#                                                          #
############################################################

# ocdcastle
# Your content goes here.
# !ocdcastle

or

////////////////////////////////////////////////////////////
//                                                        //
//           I wanna build a castle outta wood.           //
//                                                        //
////////////////////////////////////////////////////////////

// ocdcastle
// I wanna build a castle outta wood.
// !ocdcastle

Disabling the comment spacing within a block.
# OCD Disabled
# Any content here won't be parsed. # So this string won't be spaced.
# OCD Enabled

OCDFort
Smaller code dividers.

############################################################
# ocdfort

////////////////////////////////////////////////////////////
// ocdfort

Editor-agnostic.

License
This program is distributed under the GNU GPL v3 license.

Want a new feature? Contact me or perform a pull request. Anything that makes our lives simpler is welcome.