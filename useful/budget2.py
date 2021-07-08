#! python3
#budget2.py -Updated budget program using web scraping to automatically 
#determine if unit is in M deck and calculate budget

import requests, sys, webbrowser, bs4 ,logging, re, pyperclip
from lxml import etree
logging.basicConfig(level=logging.CRITICAL, format='%(asctime)s - %(levelname) s - %(message)s')

logging.debug("Program Start")
deck = "None"
if(len(sys.argv)  <2):
    logging.critical("ERROR: Not enough arguments")
    print("\nUSAGE: budget2 <SKU>   - Only accepts one sku as an argument")
    sys.exit()
if(len(sys.argv) > 2):
    logging.critical("More than one argument detected")
    sys.exit()
sku = str(sys.argv[1])
logging.debug(sku)

print(f"Searching for #{sys.argv[1]}...")
#request URL for proper SKU search
res = requests.get("https://productstation.microcenter.com/ProductStation/search_results.aspx?ntk=P_ShortSku&Ntt=" + ''.join(sys.argv[1]))
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, "lxml")
#Select relevant table 
right = soup.select("#psproduct-inventory > div > table > tbody > tr > td")
reg =re.compile(r'^[A-Za-z]$')
#Loop through matches
for item in right:
    if re.match(reg, item.text) != None: #match returns None type if no match
        deck = re.match(reg, item.text).string #Note must convert result set to text
        logging.debug("deck = " + deck) # and match object to string
        
#Determine Price
try:
    price = soup.select("#pricing")[0].text
except IndexError:
    logging.critical("ERROR: No price found on page! Confirm SKU")
    sys.exit()
#Split into list to add period and take number
priceList = list(price)
priceList.insert(-2, '.') #insert period for cents
price = ''.join(priceList)
print('Price of unit is ' + str(price))
logging.debug("price: " + str(price))
#Remove $ for budget calculations
budget = price[1:]
budget = float(budget)
logging.debug("budget: " + str(budget))
logging.debug("Is deck == M? " + str(deck == 'M'))
logging.debug("Deck: " + deck)
#Determine which percentage to apply
if deck == "M":
    budget *= .6
else:
    budget *= .8
logging.debug('Budget post calculation: ' + str(budget))

print(f"Item #{sys.argv[1]} is on {deck} deck.")

#Copy budget to clipboard
pyperclip.copy(str(round(budget,2)))
print("Budget of $%s has been copied to clipboard."% str(round(budget,2)))
webbrowser.open("https://productstation.microcenter.com/ProductStation/search_results.aspx?ntk=P_ShortSku&Ntt=" + ''.join(sys.argv[1]))