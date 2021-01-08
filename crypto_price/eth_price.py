import requests 
import json
from bs4 import BeautifulSoup 
import pywhatkit # <--for whatsapp notification, no api required

def get_price():
   
    URL = "https://coinmarketcap.com/currencies/ethereum/markets/"
    r = requests.get(URL) 
    soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib 
    data = json.loads(soup.find('script', type='application/ld+json').text)
    current_price = data['currentExchangeRate']['price']
    return current_price 

def get_notification():
    current_price = get_price()
    if current_price < 750:
        send_note = pywhatkit.sendwhatmsg("Enter your phone number","Time to buy",19,15)
        print("time to sell")
        
    return

if __name__=='__main__':
    get_notification()
    