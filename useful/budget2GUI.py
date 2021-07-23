#! python3
#budget2GUI.py -Updated budget program from command line to GUI application.
import PySimpleGUI as sg
import requests, webbrowser, bs4 ,logging, re, pyperclip, base64
from lxml import etree
from data import images
logging.basicConfig(level=logging.CRITICAL, format='%(asctime)s - %(levelname) s - %(message)s')

#Icon

#Theme
sg.theme('DarkGrey14')
sg.theme_element_background_color(color='#24292E')
sg.theme_input_background_color('#414B54')
#Set layout for GUI window
layout = [[ sg.Text('Input SKU:',size =(45, 1), justification = 'center', key='-OUTPUT-')],
          [sg.Input(key='-IN-', justification='center', focus=True)],
          [sg.Button('Search', bind_return_key= True, s=(7,1)),sg.Button('Clear',s=(7,1))]]
#Create Window

window = sg.Window('SKU Budget Check', layout, element_justification='center',
                   icon = images)
#string to store updated output 
outputStr =''
SKUERROR = 'ERROR: No price found on page! Confirm SKU'
while True: #Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED:
        break
    if event == 'Clear':
        window['-IN-'].update('')
    if event == 'Search':
        #Update window with SKU
       
        window['-OUTPUT-'].update(values['-IN-'])
        SKU = values['-IN-']
        
        res = requests.get("https://productstation.microcenter.com/ProductStation/search_results.aspx?ntk=P_ShortSku&Ntt=" + ''.join(SKU))
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text, "lxml")
        #Select relevant table 
        right = soup.select("#psproduct-inventory > div > table > tbody > tr > td")
        #Regex for price
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
            logging.critical(SKUERROR)
            window['-OUTPUT-'].update(SKUERROR)
            window['-OUTPUT-'].set_size((45, 2))
            
            continue
        #Split into list to add period and take number
        priceList = list(price)
        priceList.insert(-2, '.') #insert period for cents
        price = ''.join(priceList)
        outputStr = 'Price of unit is ' + str(price) + '\n'
        logging.debug("price: " + str(price))
        #Remove $ for budget calculations
        budget = price[1:]
        if "," in budget:
            budget = budget.replace(',', '')
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

        outputStr += f"Item #{SKU} is on {deck} deck. \n"

        #Copy budget to clipboard
        pyperclip.copy(str(round(budget,2)))
        outputStr += "Budget of $%s has been copied to clipboard."% str(round(budget,2))
        window['-OUTPUT-'].update(outputStr)
        window['-OUTPUT-'].set_size((45, 3))
        webbrowser.open("https://productstation.microcenter.com/ProductStation/search_results.aspx?ntk=P_ShortSku&Ntt=" + ''.join(SKU))        
        

#Close window after Exit or X is clicked
window.close()
















