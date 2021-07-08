#! python3
# seachpypi.py - opens multiple search results at once

import requests, sys, webbrowser, bs4 ,logging
logging.basicConfig(level=logging.CRITICAL, format='%(asctime)s - %(levelname) s - %(message)s')

print('Searching...') #Print while downloading results
res = requests.get('https://pypi.org/search/?q=' + ''.join(sys.argv[1:]))
res.raise_for_status()
logging.debug('Start of program')
#Retrieve top search results links.
soup = bs4.BeautifulSoup(res.text, 'html.parser')
#Open a browser tab for each result.
linkElems = soup.select('.package-snippet') 
logging.debug('soup = ' + str(soup.getText()))
logging.debug('linkElems = ' + str(linkElems))
if len(linkElems) == 0:
    print("No results found")
    sys.exit()
numOpen = min(5,len(linkElems))
logging.debug('numOpen = ' + str(numOpen))
for i in range(numOpen):
    urlToOpen ='https://pypi.org' +linkElems[i].get('href')
    print('Opening', urlToOpen)
    webbrowser.open(urlToOpen)
    
