# Automate The Boring Stuff
import re

phoneRegex = re.compile(r"""(
    (\d{3}|\(d{3}\))?          #Area Code
    (\s|-|\.)?                 #Separator
    \d{3}                      #First 3 digits
    (\s|-|\.)?                 #Separator
    \d{4}                      #Last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})? #Extension
)""", re.VERBOSE)

