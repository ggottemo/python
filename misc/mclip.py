#! python 3
# mclip.py - A multi-clipboard program.
# From Automate the Boring Stuff

TEXT = {'agree': '''Yes, I agree. That sounds fine to me.''',
        'busy': ''' Sorry, can we do this later this week or net week? ''',
        'upsell': '''Would you consider making this a monthly donation?'''}

## Handliung command line arguments

import sys, pyperclip
if len(sys.argv) < 2:
    #checks that there are enough arguments 
    print('Usage: python mclip.py [keyphrase] - copy phrase text' )
    sys.exit()

keyphrase = sys.argv[1] # first command line arg is the keyphrase

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print('Text for %s copied to clipboard.' % (keyphrase))
else:
    print('There is no text for ' + keyphrase)
