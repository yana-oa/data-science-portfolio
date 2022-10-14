## Web Scraping Stoic Quotes Using Python##
##           2022-10-14                  ##
##              yani                     ##

#importing libraries
from bs4 import BeautifulSoup
import pandas as pd
import requests
import urllib.request

#List to store scraped data
authors = []
quotes = []

# URL = 'https://www.goodreads.com/quotes/tag/stoicism?page=2'
# webpage = requests.get(URL) #send request to the website
# soup = BeautifulSoup(webpage.text, 'html.parser') #parse the text from the website
# quoteText = soup.find_all('div', attrs={'class':'quoteText'})

#Data Cleaning / Stripping text for quotes

# for i in quoteText:
#     quote = i.text.strip().split('\n')[0]
#     print(quote)
#     author = i.find('span', attrs={'class':'authorOrTitle'}).text.strip()
#     print(author)

#Turning the Web Scraper into a function with Page Number argument
def quote_scraper(pagenum):
    URL = 'https://www.goodreads.com/quotes/tag/stoicism?page=' + str(pagenum)
    webpage = requests.get(URL) #send request to the website
    soup = BeautifulSoup(webpage.text, 'html.parser') #parse the text from the website
    quoteText = soup.find_all('div', attrs={'class':'quoteText'})

    for i in quoteText:
        quote = i.text.strip().split('\n')[0]
        print(quote)
        author = i.find('span', attrs={'class':'authorOrTitle'}).text.strip().replace(',',"")
        print(author)
        
quote_scraper(2)
